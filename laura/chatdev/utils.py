import html
import logging
import re
import time
import sys
import threading

import markdown
import inspect
from laura.camel.messages.system_messages import SystemMessage
from laura.online_log.app import send_msg

class Loader:
    def __init__(self, duration=3, length=10):
        self.duration = duration
        self.length = length
        self._stop_event = threading.Event()

    def start(self):
        self._stop_event.clear()
        threading.Thread(target=self._run).start()

    def stop(self):
        self._stop_event.set()

    def _run(self):
        start_time = time.time()
        while not self._stop_event.is_set() and time.time() - start_time < self.duration:
            # Move the colon to the right
            for i in range(self.length - 1):
                loader = ' ' * i + '▄' + ' ' * (self.length - 1 - i)
                sys.stdout.write(f"\r{loader}")
                sys.stdout.flush()
                time.sleep(0.2)

            # Move the colon to the left
            for i in range(self.length - 1, 0, -1):
                loader = ' ' * i + '▄' + ' ' * (self.length - 1 - i)
                sys.stdout.write(f"\r{loader}")
                sys.stdout.flush()
                time.sleep(0.2)

        sys.stdout.write("\r" + " " * self.length + "\r")  # Clear the loader

def now():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())

loader = Loader(duration=2)  # Create a loader instance

def log_and_print_online(role, content=None):
    global loader

    # Stop the previous loader and clear its output
    loader.stop()
    sys.stdout.write("\r" + " " * loader.length + "\r")
    sys.stdout.flush()

    # Start a new loader
    loader = Loader(duration=2)
    loader.start()

    if not content:
        logging.info(role + "\n")
        send_msg("Laura", role)
        print(role + "\n")
    else:
        print("Finished talking with " + str(role) + "\n")
        logging.info(str(role) + "\n")
        if isinstance(content, SystemMessage):
            records_kv = []
            content.meta_dict["content"] = content.content
            for key in content.meta_dict:
                value = content.meta_dict[key]
                value = str(value)
                value = html.unescape(value)
                value = markdown.markdown(value)
                value = re.sub(r'<[^>]*>', '', value)
                value = value.replace("\n", " ")
                records_kv.append([key, value])
            content = "[SystemMessage]\n\n" + convert_to_markdown_table(records_kv)
        else:
            role = str(role)
            content = str(content)
        send_msg(role, content)


def convert_to_markdown_table(records_kv):
    # Create the Markdown table header
    header = "| Parameter | Value |\n| --- | --- |"

    # Create the Markdown table rows
    rows = [f"| **{key}** | {value} |" for (key, value) in records_kv]

    # Combine the header and rows to form the final Markdown table
    markdown_table = header + "\n" + '\n'.join(rows)

    return markdown_table


def log_arguments(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        params = sig.parameters

        all_args = {}
        all_args.update({name: value for name, value in zip(params.keys(), args)})
        all_args.update(kwargs)

        records_kv = []
        for name, value in all_args.items():
            if name in ["self", "chat_env", "task_type"]:
                continue
            value = str(value)
            value = html.unescape(value)
            value = markdown.markdown(value)
            value = re.sub(r'<[^>]*>', '', value)
            value = value.replace("\n", " ")
            records_kv.append([name, value])
        records = f"**[{func.__name__}]**\n\n" + convert_to_markdown_table(records_kv)
        log_and_print_online("Laura", records)

        return func(*args, **kwargs)

    return wrapper
