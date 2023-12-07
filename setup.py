import os
import shutil
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    """Custom installation script to install the package and then copy the frameworks folder."""
    description = 'Install the package and copy the frameworks folder'

    def run(self):
        # First, run the standard install
        install.run(self)

        # Then, copy the frameworks folder
        project_config_source = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'laura', 'frameworks')
        home_directory = os.path.expanduser('~')
        project_config_destination = os.path.join(home_directory, 'laura', 'frameworks')

        if not os.path.exists(project_config_destination):
            os.makedirs(project_config_destination, exist_ok=True)

        if os.path.exists(project_config_source) and os.path.isdir(project_config_source):
            for item in os.listdir(project_config_source):
                src_path = os.path.join(project_config_source, item)
                dst_path = os.path.join(project_config_destination, item)
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                else:
                    shutil.copy2(src_path, dst_path)

        print("Installation complete. frameworks folder has been copied to:", project_config_destination)

setup(
    name='Laura',
    version='1.0',  # Replace with your project's version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama==0.4.6',
        'Flask==2.3.2',
        'Flask-SocketIO==5.3.4',
        'importlib-metadata==6.8.0',
        'numpy==1.24.3',
        'openai==0.27.8',
        'regex==2023.6.3',
        'requests==2.31.0',
        'tenacity==8.2.2',
        'tiktoken==0.4.0',
        'virtualenv==20.23.0',
        'Werkzeug==2.3.6',
        'Markdown==3.4.4',
        'Pillow==10.1.0'
    ],
    entry_points={
        'console_scripts': [
            'laura=laura.run:main',
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    }
)
