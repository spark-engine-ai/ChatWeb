import subprocess
import sys

def main():
    print("Starting installation process...")
    subprocess.call(['pip', 'install', 'dist/Laura-1.0.tar.gz'])
    print("Success! You have installed the project.")

if __name__ == "__main__":
    print("Executing install.py script...")
    main()
