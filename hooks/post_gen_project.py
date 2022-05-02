import os
import sys
import subprocess

project_dir = os.getcwd()

# project_slug =  "{{ cookiecutter.__project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[94m"
RESET_ALL = "\x1b[0m"

REMOVE_PATHS = [
    '{% if cookiecutter.project_packages != "All" -%} tasks.py {% endif -%}',
    '{% if cookiecutter.env_tool == "conda" -%} requirements.txt {% endif -%}',
    '{% if cookiecutter.env_tool == "pip" -%} environment.yml {% endif -%}',
    '{% if cookiecutter.project_open_source_license == "No license file" -%} LICENSE {% endif -%}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

print(f"{MESSAGE_COLOR}almost done!")

# print(f'Initializing a git repository...{RESET_ALL}')
# subprocess.call(['git', 'init'])
# subprocess.call(['git', 'add', '*'])
# subprocess.call(['git', 'commit', '-m', 'Initial commit'])
# subprocess.call(['git', 'branch', '-M', 'main'])

print(f"{MESSAGE_COLOR}Done! Let's get started {RESET_ALL}")