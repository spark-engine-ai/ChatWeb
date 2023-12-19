# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, webapplication
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import argparse
import logging
import os
import sys
import json
from pathlib import Path

from laura.camel.typing import ModelType

root = os.path.dirname(__file__)
sys.path.append(root)

from laura.chatdev.chat_chain import ChatChain

def main(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)


parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('--config', type=str, default="Human",
                    help="Name of config, which is used to load configuration under CompanyConfig/")
parser.add_argument('--org', type=str, default="Organization",
                    help="Name of organization, your web application will be generated in projects/name_org_timestamp")
parser.add_argument('--task', type=str, default="Develop a basic landing page.",
                    help="Prompt of web application")
parser.add_argument('--name', type=str, default="LAuRA",
                    help="Name of web application, your web application will be generated in projects/name_org_timestamp")
parser.add_argument('--model', type=str, default="GPT_3_5_TURBO",
                    help="GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}")
parser.add_argument('--path', type=str, default="",
                    help="Your file directory, LAuRA will build upon your web application in the Incremental mode")
parser.add_argument('--stack', type=str, default="NEXT",
                    help="Stack configuration file name under frameworks/")
args = parser.parse_args()

# ASCII Art for LAuRA
laura_ascii_art = """
    ___________________________________________

    ██╗      █████╗ ██╗   ██╗██████╗  █████╗
    ██║     ██╔══██╗██║   ██║██╔══██╗██╔══██╗
    ██║     ███████║██║   ██║██████╔╝███████║
    ██║     ██╔══██║██║   ██║██╔══██╗██╔══██║
    ███████╗██║  ██║╚██████╔╝██║  ██║██║  ██║
    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

    (Loop Automated React Architecture)
    ___________________________________________

    Laura is an AI-driven workforce dedicated to automating the process of
    building websites and web applications.

    Created by Spark Engine
    URL: https://laura.sparkengine.ai


    Need help? Use 'laura -h' for our full list of arguments, or begin below.

"""

# Welcome message
print(laura_ascii_art)

# Check if no arguments were provided
if len(sys.argv) == 1:
    args.name = input("Name your project => ").strip()
    while not args.name:
        args.name = input("Name of the web application cannot be blank, please enter again => ").strip()
    args.task = input("\nWhat would you like to build? => ").strip()
    while not args.task:
        args.task = input("Prompt of the web application cannot be blank, please enter again => ").strip()
    # Additional prompts can be uncommented and used as needed
    # args.config = input("Which mode would you like to use? -> ") or "Human"
    # args.model = input("Enter the GPT Model: ") or "GPT_3_5_TURBO"
    # args.path = input("Enter your file directory [default path]: ") or ""
    # Code to list configurations
    home_directory = Path.home()
    frameworks_dir = home_directory / "laura" / "frameworks"
    print("\nConfigurations:\n")
    for config_file in frameworks_dir.glob("*.json"):
        with open(config_file, 'r') as file:
            config = json.load(file)
        print(f"<<< {config_file.stem} >>>")
        print(f"Framework: {config.get('framework', 'Unknown Framework')}")
        print(f"UI Kit: {config.get('ui_kit', 'Unknown UI Kit')}\n")

    args.stack = input("\nEnter your preferred stack configuration (default is REACT) => ") or "REACT"

if "OPENAI_API_KEY" not in os.environ:
    sys.exit("\nOops!\nYour OPENAI_API_KEY is not set. Please set it in your environment variables.\n")
# New code to read JSON configuration file and update task argument
home_directory = Path.home()
stack_config_file = home_directory / "laura" / "frameworks" / f"{args.stack}.json"
if stack_config_file.exists():
    with open(stack_config_file, 'r') as file:
        stack_config = json.load(file)
    ui_kit = stack_config.get("ui_kit", "Tailwind UI Kit classes")
    framework = stack_config.get("framework", "React JS")
    args.task += f". Keep in mind we are using {ui_kit} with {framework}."
else:
    print(f"Warning: Stack configuration file {args.stack}.json not found in {stack_config_file}. Proceeding with default values.")

# Start ChatDev

# ----------------------------------------
#          Init ChatChain
# ----------------------------------------
config_path, config_phase_path, config_role_path = main(args.config)
args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO, 'GPT_4': ModelType.GPT_4, 'GPT_4_32K': ModelType.GPT_4_32k}
chat_chain = ChatChain(config_path=config_path,
                       config_phase_path=config_phase_path,
                       config_role_path=config_role_path,
                       task_prompt=args.task,
                       project_name=args.name,
                       org_name=args.org,
                       model_type=args2type[args.model],
                       code_path=args.path,
                       stack_config=args.stack)

# ----------------------------------------
#          Init Log
# ----------------------------------------
logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")

# ----------------------------------------
#          Pre Processing
# ----------------------------------------

chat_chain.pre_processing()

# ----------------------------------------
#          Personnel Recruitment
# ----------------------------------------

chat_chain.make_recruitment()

# ----------------------------------------
#          Chat Chain
# ----------------------------------------

chat_chain.execute_chain()

# ----------------------------------------
#          Post Processing
# ----------------------------------------

chat_chain.post_processing()
