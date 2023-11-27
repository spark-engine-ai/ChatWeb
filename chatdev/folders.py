import os
import re
from colorama import Fore

class Folders():
    def __init__(self, generated_content="", parse=True):
        self.generated_folders = set()

        if generated_content:
            if parse:
                self._parse_content(generated_content)
            else:
                self.generated_folders.add(generated_content)

    def _parse_content(self, content):
        regex = r"```\n(.*?)```"
        matches = re.finditer(regex, content, re.DOTALL)
        for match in matches:
            folder_name = match.group(1).strip()
            self.generated_folders.add(folder_name)

    def _update_folders(self, generated_content, parse=True):
        new_folders = Folders(generated_content, parse)
        for folder in new_folders.generated_folders:
            if folder not in self.generated_folders:
                print("{} added.".format(folder))
                self.generated_folders.add(folder)

    def _create_folders(self):
        for folder in self.generated_folders:
            if not os.path.exists(folder):
                os.mkdir(folder)
                print("{} Created.".format(folder))

    def _get_folders(self):
        return "\n".join(self.generated_folders)
