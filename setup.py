import os
import shutil
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    """Custom installation script to install the package and then copy the frameworks folder."""
    description = 'Install the package and copy the frameworks folder'

    def run(self):
        # First, run the standard install
        install.run(self)

        # Then, copy the frameworks folder
        project_config_source = Path(__file__).parent / 'laura' / 'frameworks'
        home_directory = Path.home()
        project_config_destination = home_directory / 'laura' / 'frameworks'

        # Create destination directory if it doesn't exist
        project_config_destination.mkdir(parents=True, exist_ok=True)

        # Copy the files
        for item in project_config_source.iterdir():
            dest_path = project_config_destination / item.name
            if item.is_dir():
                shutil.copytree(item, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest_path)

        print(f"Installation complete. frameworks folder has been copied to: {project_config_destination}")

setup(
    name='Laura',
    version='1.0',  # Replace with your project's version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama==0.4.6',
        'tenacity==8.2.3',
        'Flask==2.3.2',
        'Flask-SocketIO==5.3.4',
        'importlib-metadata==6.8.0',
        'numpy==1.24.3',
        'openai==0.27.8',
        'regex==2023.6.3',
        'requests==2.31.0',
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
