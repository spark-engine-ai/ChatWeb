import importlib
import json
import logging
import os
import shutil
import time
from datetime import datetime

from camel.agents import RolePlaying
from camel.configs import ChatGPTConfig
from camel.typing import TaskType, ModelType
from chatdev.chat_env import ChatEnv, ChatEnvConfig
from chatdev.statistics import get_info
from chatdev.utils import log_and_print_online, now


def check_bool(s):
    return s.lower() == "true"


class ChatChain:

    def __init__(self,
                 config_path: str = None,
                 config_phase_path: str = None,
                 config_role_path: str = None,
                 task_prompt: str = None,
                 project_name: str = None,
                 org_name: str = None,
                 model_type: ModelType = ModelType.GPT_3_5_TURBO,
                 code_path: str = None) -> None:
        """

        Args:
            config_path: path to the ChatChainConfig.json
            config_phase_path: path to the PhaseConfig.json
            config_role_path: path to the RoleConfig.json
            task_prompt: the user input prompt for webapplication
            project_name: the user input name for webapplication
            org_name: the organization name of the human user
        """

        # load config file
        self.config_path = config_path
        self.config_phase_path = config_phase_path
        self.config_role_path = config_role_path
        self.project_name = project_name
        self.org_name = org_name
        self.model_type = model_type
        self.code_path = code_path

        with open(self.config_path, 'r', encoding="utf8") as file:
            self.config = json.load(file)
        with open(self.config_phase_path, 'r', encoding="utf8") as file:
            self.config_phase = json.load(file)
        with open(self.config_role_path, 'r', encoding="utf8") as file:
            self.config_role = json.load(file)

        # init chatchain config and recruitments
        self.chain = self.config["chain"]
        self.recruitments = self.config["recruitments"]

        # init default max chat turn
        self.chat_turn_limit_default = 10

        # init ChatEnv
        self.chat_env_config = ChatEnvConfig(clear_structure=check_bool(self.config["clear_structure"]),
                                             gui_design=check_bool(self.config["gui_design"]),
                                             git_management=check_bool(self.config["git_management"]),
                                             incremental_develop=check_bool(self.config["incremental_develop"]))
        self.chat_env = ChatEnv(self.chat_env_config)

        # the user input prompt will be self-improved (if set "self_improve": "True" in ChatChainConfig.json)
        # the self-improvement is done in self.preprocess
        self.task_prompt_raw = task_prompt
        self.task_prompt = ""

        # init role prompts
        self.role_prompts = dict()
        for role in self.config_role:
            self.role_prompts[role] = "\n".join(self.config_role[role])

        # init log
        self.start_time, self.log_filepath = self.get_logfilepath()

        # init SimplePhase instances
        # import all used phases in PhaseConfig.json from chatdev.phase
        # note that in PhaseConfig.json there only exist SimplePhases
        # ComposedPhases are defined in ChatChainConfig.json and will be imported in self.execute_step
        self.compose_phase_module = importlib.import_module("chatdev.composed_phase")
        self.phase_module = importlib.import_module("chatdev.phase")
        self.phases = dict()
        for phase in self.config_phase:
            assistant_role_name = self.config_phase[phase]['assistant_role_name']
            user_role_name = self.config_phase[phase]['user_role_name']
            phase_prompt = "\n\n".join(self.config_phase[phase]['phase_prompt'])
            phase_class = getattr(self.phase_module, phase)
            phase_instance = phase_class(assistant_role_name=assistant_role_name,
                                         user_role_name=user_role_name,
                                         phase_prompt=phase_prompt,
                                         role_prompts=self.role_prompts,
                                         phase_name=phase,
                                         model_type=self.model_type,
                                         log_filepath=self.log_filepath)
            self.phases[phase] = phase_instance

    def make_recruitment(self):
        """
        recruit all employees
        Returns: None

        """
        for employee in self.recruitments:
            self.chat_env.recruit(agent_name=employee)

    def execute_step(self, phase_item: dict):
        """
        execute single phase in the chain
        Args:
            phase_item: single phase configuration in the ChatChainConfig.json

        Returns:

        """

        phase = phase_item['phase']
        phase_type = phase_item['phaseType']
        # For SimplePhase, just look it up from self.phases and conduct the "Phase.execute" method
        if phase_type == "SimplePhase":
            max_turn_step = phase_item['max_turn_step']
            need_reflect = check_bool(phase_item['need_reflect'])
            if phase in self.phases:
                self.chat_env = self.phases[phase].execute(self.chat_env,
                                                           self.chat_turn_limit_default if max_turn_step <= 0 else max_turn_step,
                                                           need_reflect)
            else:
                raise RuntimeError(f"Phase '{phase}' is not yet implemented in chatdev.phase")
        # For ComposedPhase, we create instance here then conduct the "ComposedPhase.execute" method
        elif phase_type == "ComposedPhase":
            cycle_num = phase_item['cycleNum']
            composition = phase_item['Composition']
            compose_phase_class = getattr(self.compose_phase_module, phase)
            if not compose_phase_class:
                raise RuntimeError(f"Phase '{phase}' is not yet implemented in chatdev.compose_phase")
            compose_phase_instance = compose_phase_class(phase_name=phase,
                                                         cycle_num=cycle_num,
                                                         composition=composition,
                                                         config_phase=self.config_phase,
                                                         config_role=self.config_role,
                                                         model_type=self.model_type,
                                                         log_filepath=self.log_filepath)
            self.chat_env = compose_phase_instance.execute(self.chat_env)
        else:
            raise RuntimeError(f"PhaseType '{phase_type}' is not yet implemented.")

    def execute_chain(self):
        """
        execute the whole chain based on ChatChainConfig.json
        Returns: None

        """
        for phase_item in self.chain:
            self.execute_step(phase_item)

    def get_logfilepath(self):
        """
        get the log path (under the webapplication path)
        Returns:
            start_time: time for starting making the webapplication
            log_filepath: path to the log

        """
        start_time = now()
        filepath = os.path.dirname(__file__)
        # root = "/".join(filepath.split("/")[:-1])
        root = os.path.dirname(filepath)
        # directory = root + "/ProjectOutput/"
        directory = os.path.join(root, "ProjectOutput")
        log_filepath = os.path.join(directory,
                                    "{}.log".format("_".join([self.project_name, self.org_name, start_time])))
        return start_time, log_filepath

    def pre_processing(self):
        """
        remove useless files and log some global config settings
        Returns: None

        """
        if self.chat_env.config.clear_structure:
            filepath = os.path.dirname(__file__)
            root = os.path.dirname(filepath)
            directory = os.path.join(root, "ProjectOutput")
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                # logs with error trials are left in ProjectOutput/
                if os.path.isfile(file_path) and not filename.endswith(".js") and not filename.endswith(".log"):
                    os.remove(file_path)
                    print("{} Removed.".format(file_path))

        webapplication_path = os.path.join(directory, "_".join([self.project_name, self.org_name, self.start_time]))
        self.chat_env.set_directory(webapplication_path)

        # Create specific subdirectories for Next.js TypeScript project
        subdirectories = ["components", "public", "pages", "context", "types", "styles"]
        for subdirectory in subdirectories:
            path = os.path.join(webapplication_path, subdirectory)
            os.makedirs(path, exist_ok=True)
            print(f"Subdirectory '{subdirectory}' created at {path}")

        nextjs_typescript_tailwind_config = {
            "next.config.js": "module.exports = {\n  reactStrictMode: true,\n};\n",
            "tsconfig.json": "{\n  \"compilerOptions\": {\n    \"target\": \"es5\",\n    \"lib\": [\"dom\", \"dom.iterable\", \"esnext\"],\n    \"allowJs\": true,\n    \"skipLibCheck\": true,\n    \"strict\": false,\n    \"forceConsistentCasingInFileNames\": true,\n    \"noEmit\": true,\n    \"esModuleInterop\": true,\n    \"module\": \"esnext\",\n    \"moduleResolution\": \"node\",\n    \"resolveJsonModule\": true,\n    \"isolatedModules\": true,\n    \"jsx\": \"preserve\"\n  },\n  \"include\": [\"next-env.d.ts\", \"**/*.ts\", \"**/*.tsx\"],\n  \"exclude\": [\"node_modules\"]\n}",
            "package.json": "{\n  \"name\": \"" + self.project_name + "\",\n  \"version\": \"1.0.0\",\n  \"description\": \"Website landing page built with React and Tailwind\",\n  \"scripts\": {\n    \"dev\": \"next dev\",\n    \"build\": \"next build\",\n    \"start\": \"next start\"\n  },\n  \"dependencies\": {\n    \"autoprefixer\": \"^10.4.16\",\n   \"next\": \"^13.2.4\",\n    \"postcss\": \"^8.4.31\",\n    \"react\": \"^18.2.0\",\n    \"react-dom\": \"^18.2.0\",\n    \"react-icons\": \"^4.12.0\"\n  },\n  \"devDependencies\":      {\n    \"@types/react\": \"^18.0.28\",\n    \"react-scripts\": \"^5.0.1\",\n    \"tailwindcss\": \"^3.3.5\",\n    \"typescript\": \"^4.9.5\"\n  },\n  \"browserslist\": {\n    \"production\": [\n      \">0.2%\",\n      \"not dead\",\n      \"not op_mini all\"\n    ],\n    \"development\": [\n      \"last 1 chrome version\",\n      \"last 1 firefox version\",\n      \"last 1 safari version\"\n    ]\n  }\n}",
            "tailwind.config.js": "module.exports = {\n  content: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],\n  darkMode: false, // or 'media' or 'class'\n  theme: {\n    extend: {},\n  },\n  variants: {\n    extend: {},\n  },\n  plugins: [],\n};\n",
            ".env": "# Environment variables\n# e.g., API_KEY=yourapikey\n",
            ".gitignore": "node_modules/\n.next/\nout/\n*.log\n.env.local\n.env.development.local\n.env.test.local\n.env.production.local\n",
            "postcss.config.js": "module.exports = {\n  plugins: {\n    tailwindcss: {},\n    autoprefixer: {},\n  },\n};\n",
            "next-env.d.ts": "// <reference types=\"next\" />\n// <reference types=\"next/types/global\" />\n",
            "README.md": f"# {self.project_name}\n\nThis is a [Next.js](https://nextjs.org/) project bootstrapped with TypeScript and Tailwind CSS.\n\n## Getting Started\n\nFirst, run the development server:\n\n```bash\nnpm run dev\n# or\nyarn dev\n```\n\nOpen [http://localhost:3000](http://localhost:3000) with your browser to see the result.\n\n...",
            os.path.join("pages", "_app.tsx"): "import '../styles/globals.css'\n\nfunction MyApp({ Component, pageProps }) {\n  return <Component {...pageProps} />\n}\n\nexport default MyApp\n",
            os.path.join("pages", "_document.tsx"): "import Document, { Html, Head, Main, NextScript } from 'next/document'\n\nclass MyDocument extends Document {\n  render() {\n    return (\n      <Html>\n        <Head />\n        <body>\n          <Main />\n          <NextScript />\n        </body>\n      </Html>\n    )\n  }\n}\n\nexport default MyDocument\n",
            os.path.join("pages", "index.tsx"): "import MainComponent from '../components/main'\n\nexport default function Home() {\n  return <MainComponent />\n}\n",
            os.path.join("pages", "404.tsx"): "export default function Custom404() {\n  return <h1>404 - Page Not Found</h1>\n}\n",
            os.path.join("styles", "globals.css"): "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n\nbody {\n  margin: 0;\n  padding: 0;\n  box-sizing: border-box;\n}\n"
        }

        for file_name, content in nextjs_typescript_tailwind_config.items():
            file_path = os.path.join(webapplication_path, file_name)
            with open(file_path, "w") as file:
                file.write(content)
                print(f"{file_name} created with starter content at {file_path}")

        # copy config files to webapplication path
        shutil.copy(self.config_path, webapplication_path)
        shutil.copy(self.config_phase_path, webapplication_path)
        shutil.copy(self.config_role_path, webapplication_path)

        # copy code files to webapplication path in incremental_develop mode
        if check_bool(self.config["incremental_develop"]):
            for root, dirs, files in os.walk(self.code_path):
                relative_path = os.path.relpath(root, self.code_path)
                target_dir = os.path.join(webapplication_path, 'base', relative_path)
                os.makedirs(target_dir, exist_ok=True)
                for file in files:
                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_dir, file)
                    shutil.copy2(source_file, target_file)
            self.chat_env._load_from_hardware(os.path.join(webapplication_path, 'base'))

        # write task prompt to webapplication
        with open(os.path.join(webapplication_path, self.project_name + ".prompt"), "w") as f:
            f.write(self.task_prompt_raw)

        preprocess_msg = "**[Preprocessing]**\n\n"
        chat_gpt_config = ChatGPTConfig()

        preprocess_msg += "**ChatDev Starts** ({})\n\n".format(self.start_time)
        preprocess_msg += "**Timestamp**: {}\n\n".format(self.start_time)
        preprocess_msg += "**config_path**: {}\n\n".format(self.config_path)
        preprocess_msg += "**config_phase_path**: {}\n\n".format(self.config_phase_path)
        preprocess_msg += "**config_role_path**: {}\n\n".format(self.config_role_path)
        preprocess_msg += "**task_prompt**: {}\n\n".format(self.task_prompt_raw)
        preprocess_msg += "**project_name**: {}\n\n".format(self.project_name)
        preprocess_msg += "**Log File**: {}\n\n".format(self.log_filepath)
        preprocess_msg += "**ChatDevConfig**:\n{}\n\n".format(self.chat_env.config.__str__())
        preprocess_msg += "**ChatGPTConfig**:\n{}\n\n".format(chat_gpt_config)
        log_and_print_online(preprocess_msg)

        # init task prompt
        if check_bool(self.config['self_improve']):
            self.chat_env.env_dict['task_prompt'] = self.self_task_improve(self.task_prompt_raw)
        else:
            self.chat_env.env_dict['task_prompt'] = self.task_prompt_raw

    def post_processing(self):
        """
        summarize the production and move log files to the webapplication directory
        Returns: None

        """

        self.chat_env.write_meta()
        filepath = os.path.dirname(__file__)
        root = os.path.dirname(filepath)

        if self.chat_env_config.git_management:
            git_online_log = "**[Git Information]**\n\n"

            self.chat_env.codes.version += 1
            os.system("cd {}; git add .".format(self.chat_env.env_dict["directory"]))
            git_online_log += "cd {}; git add .\n".format(self.chat_env.env_dict["directory"])
            os.system("cd {}; git commit -m \"v{} Final Version\"".format(self.chat_env.env_dict["directory"], self.chat_env.codes.version))
            git_online_log += "cd {}; git commit -m \"v{} Final Version\"\n".format(self.chat_env.env_dict["directory"], self.chat_env.codes.version)
            log_and_print_online(git_online_log)

            git_info = "**[Git Log]**\n\n"
            import subprocess

            # execute git log
            command = "cd {}; git log".format(self.chat_env.env_dict["directory"])
            completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE)

            if completed_process.returncode == 0:
                log_output = completed_process.stdout
            else:
                log_output = "Error when executing " + command

            git_info += log_output
            log_and_print_online(git_info)

        post_info = "**[Post Info]**\n\n"
        now_time = now()
        time_format = "%Y%m%d%H%M%S"
        datetime1 = datetime.strptime(self.start_time, time_format)
        datetime2 = datetime.strptime(now_time, time_format)
        duration = (datetime2 - datetime1).total_seconds()

        post_info += "Software Info: {}".format(
            get_info(self.chat_env.env_dict['directory'], self.log_filepath) + "\n\n🕑**duration**={:.2f}s\n\n".format(
                duration))

        post_info += "ChatDev Starts ({})".format(self.start_time) + "\n\n"
        post_info += "ChatDev Ends ({})".format(now_time) + "\n\n"

        if self.chat_env.config.clear_structure:
            directory = self.chat_env.env_dict['directory']
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isdir(file_path) and file_path.endswith("__pycache__"):
                    shutil.rmtree(file_path, ignore_errors=True)
                    post_info += "{} Removed.".format(file_path) + "\n\n"

        log_and_print_online(post_info)

        logging.shutdown()
        time.sleep(1)

        shutil.move(self.log_filepath,
                    os.path.join(root + "/ProjectOutput", "_".join([self.project_name, self.org_name, self.start_time]), "/components",
                                 os.path.basename(self.log_filepath)))

    # @staticmethod
    def self_task_improve(self, task_prompt):
        """
        ask agent to improve the user query prompt
        Args:
            task_prompt: original user query prompt

        Returns:
            revised_task_prompt: revised prompt from the prompt engineer agent

        """
        self_task_improve_prompt = """I will give you a short description of a web application design requirement,
please rewrite it into a detailed prompt that can make large language model know how to make this web application better based this prompt,
the prompt should ensure LLMs build a webapplication that can be run correctly, which is the most import part you need to consider.
remember that the revised prompt should not contain more than 200 words,
here is the short description:\"{}\".
If the revised prompt is revised_version_of_the_description,
then you should return a message in a format like \"<INFO> revised_version_of_the_description\", do not return messages in other formats.""".format(
            task_prompt)
        role_play_session = RolePlaying(
            assistant_role_name="Prompt Engineer",
            assistant_role_prompt="You are an professional prompt engineer that can improve user input prompt to make LLM better understand these prompts.",
            user_role_prompt="You are an user that want to use LLM to build webapplication.",
            user_role_name="User",
            task_type=TaskType.CHATDEV,
            task_prompt="Do prompt engineering on user query",
            with_task_specify=False,
            model_type=self.model_type,
        )

        # log_and_print_online("System", role_play_session.assistant_sys_msg)
        # log_and_print_online("System", role_play_session.user_sys_msg)

        _, input_user_msg = role_play_session.init_chat(None, None, self_task_improve_prompt)
        assistant_response, user_response = role_play_session.step(input_user_msg, True)
        revised_task_prompt = assistant_response.msg.content.split("<INFO>")[-1].lower().strip()
        log_and_print_online(role_play_session.assistant_agent.role_name, assistant_response.msg.content)
        log_and_print_online(
            "**[Task Prompt Self Improvement]**\n**Original Task Prompt**: {}\n**Improved Task Prompt**: {}".format(
                task_prompt, revised_task_prompt))
        return revised_task_prompt
