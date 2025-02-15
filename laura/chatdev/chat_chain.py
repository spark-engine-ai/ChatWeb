import importlib
import json
import string
import logging
import os
import shutil
import time
from datetime import datetime
from pathlib import Path

from laura.camel.agents import RolePlaying
from laura.camel.configs import ChatGPTConfig
from laura.camel.typing import TaskType, ModelType
from laura.chatdev.chat_env import ChatEnv, ChatEnvConfig
from laura.chatdev.statistics import get_info
from laura.chatdev.utils import log_and_print_online, now


def check_bool(s):
    return s.lower() == "true"

class SafeFormatter(string.Formatter):
    """A formatter class that doesn't throw a KeyError for missing placeholders."""
    def get_value(self, key, args, kwargs):
        return kwargs.get(key, '{' + key + '}')

    def safe_format(self, format_string, **kwargs):
        return self.format(format_string, **kwargs)

def replace_placeholders(item, formatter, stack_config_data):
    """Recursively replace placeholders in the given item."""
    # Determine the language based on the 'typescript' flag in the stack configuration
    jslanguage = "TypeScript" if stack_config_data.get('typescript', False) else "JavaScript"

    if isinstance(item, dict):
        return {k: replace_placeholders(v, formatter, stack_config_data) for k, v in item.items()}
    elif isinstance(item, list):
        return [replace_placeholders(v, formatter, stack_config_data) for v in item]
    elif isinstance(item, str):
        # Now use 'language' as a simple placeholder
        return formatter.safe_format(
            item,
            framework=stack_config_data.get('framework', ''),
            ui_kit=stack_config_data.get('ui_kit', ''),
            jslanguage=jslanguage  # Use the computed language here
            # Additional replacements can be added here
        )
    return item

class ChatChain:

    def __init__(self,
                 config_path: str = None,
                 config_phase_path: str = None,
                 config_role_path: str = None,
                 task_prompt: str = None,
                 project_name: str = None,
                 org_name: str = None,
                 model_type: ModelType = ModelType.GPT_3_5_TURBO,
                 code_path: str = None,
                 stack_config: str = None) -> None:
        """

        Args:
            config_path: path to the ChatChainConfig.json
            config_phase_path: path to the PhaseConfig.json
            config_role_path: path to the RoleConfig.json
            task_prompt: the user input prompt for webapplication
            project_name: the user input name for webapplication
            org_name: the organization name of the human user
            stack_config: name of the stack config file in the frameworks folder (to determine the projects template)
        """

        # load config file
        self.config_path = config_path
        self.config_phase_path = config_phase_path
        self.config_role_path = config_role_path
        self.project_name = project_name
        self.org_name = org_name
        self.model_type = model_type
        self.code_path = code_path
        self.stack_config = f"{stack_config}.json"
        self.apply_stack_configuration()

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
        self.chat_env = ChatEnv(self.chat_env_config, stack_config=stack_config)

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
        # import all used phases in PhaseConfig.json from laura.chatdev.phase
        # note that in PhaseConfig.json there only exist SimplePhases
        # ComposedPhases are defined in ChatChainConfig.json and will be imported in self.execute_step
        self.compose_phase_module = importlib.import_module("laura.chatdev.composed_phase")
        self.phase_module = importlib.import_module("laura.chatdev.phase")
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

    def apply_stack_configuration(self):
        # Load the stack configuration
        home_directory = Path.home()
        template_config_path = home_directory.joinpath('laura/frameworks', self.stack_config)
        with open(template_config_path, 'r', encoding='utf-8') as file:
            self.stack_config_data = json.load(file)

        # Load the company configuration
        chat_chain_config_path = home_directory.joinpath(self.config_phase_path)

        with open(chat_chain_config_path, 'r', encoding='utf-8') as file:
            chat_chain_config_data = json.load(file)

        # Create an instance of SafeFormatter
        safe_formatter = SafeFormatter()

        # Apply the replacement function to the entire configuration
        chat_chain_config_data = replace_placeholders(chat_chain_config_data, safe_formatter, self.stack_config_data)

        # Save the modified company configuration back to a file
        with open(chat_chain_config_path, 'w') as file:
            json.dump(chat_chain_config_data, file, indent=4)

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
                raise RuntimeError(f"Phase '{phase}' is not yet implemented in laura.chatdev.phase")
        # For ComposedPhase, we create instance here then conduct the "ComposedPhase.execute" method
        elif phase_type == "ComposedPhase":
            cycle_num = phase_item['cycleNum']
            composition = phase_item['Composition']
            compose_phase_class = getattr(self.compose_phase_module, phase)
            if not compose_phase_class:
                raise RuntimeError(f"Phase '{phase}' is not yet implemented in laura.compose_phase")
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
        start_time = now()
        # Use a directory in the user's home folder
        home_directory = Path.home()
        directory = home_directory.joinpath("laura/projects")
        directory.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

        log_filename = "{}.log".format("_".join([self.project_name, self.org_name, start_time]))
        log_filepath = directory.joinpath(log_filename)
        return start_time, str(log_filepath)

    def pre_processing(self):
        """
        remove useless files and log some global config settings
        Returns: None

        """
        if self.chat_env.config.clear_structure:
            filepath = os.path.dirname(__file__)
            root = os.path.dirname(filepath)
            home_directory = Path.home()
            directory = home_directory.joinpath("laura/projects")
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                # logs with error trials are left in projects/
                if os.path.isfile(file_path) and not filename.endswith(".js") and not filename.endswith(".log"):
                    os.remove(file_path)
                    print("{} Removed.".format(file_path))

        webapplication_path = os.path.join(directory, "_".join([self.project_name, self.org_name, self.start_time]))
        self.chat_env.set_directory(webapplication_path)

        # Load the configuration for the project template
        home_directory = Path.home()
        template_config_path = home_directory.joinpath('laura/frameworks',self.stack_config)
        with open(template_config_path, 'r', encoding='utf-8') as file:
            template_config = json.load(file)

        # Define the source directory of the template files
        source_template_dir = home_directory.joinpath('laura/frameworks', template_config['template_path'])

        # Define the destination directory where the project will be set up
        destination_dir = home_directory.joinpath(directory, "_".join([self.project_name, self.org_name, self.start_time]))

        # This function will copy all files and folders recursively from the source to the destination
        def copy_template(src, dst):
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)  # dirs_exist_ok is available in Python 3.8+
            else:
                shutil.copy(src, dst)

        # Copy all files and folders from the template directory to the destination
        copy_template(source_template_dir, destination_dir)

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
        # log_and_print_online(preprocess_msg)

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
