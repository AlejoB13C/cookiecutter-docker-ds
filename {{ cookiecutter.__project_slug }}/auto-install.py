import os
import subprocess

project_dir = os.getcwd()

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[94m"
RESET_ALL = "\x1b[0m"

def environ():
    # Create the environment according to the user selection
{% if cookiecutter.env_tool == "conda" %}

    print(f"{MESSAGE_COLOR}Creating conda env (./env)...{RESET_ALL}")
    subprocess.call(["mamba", "env", "create", "--prefix", "./env", "--file", "environment.yml"])
{% elif cookiecutter.env_tool == "pip" %}

    print(f"{MESSAGE_COLOR}Creating virtualenv (./env)...{RESET_ALL}"
    subprocess.call(["python3", "-m", "venv","env"])

    pyt = f"{project_dir}/env/bin/python3"
    subprocess.call([f"{pyt}", "-m", "pip", "install", "--upgrade", "pip"])

    pip = f"{project_dir}/env/bin/pip"
    subprocess.call([f"{pip}", "install", "-r", "requirements.txt"])
{% endif %}


def nb():
    # Set up Git diff for notebooks and lab
    nbdime = 'env/bin/nbdime'
    subprocess.call([f"{nbdime}", "config-git", "--enable"]) #configure it to this git project
{% if cookiecutter.project_packages == "All" %}
    subprocess.call([f"{nbdime}", "extensions", "--enable", "--sys-prefix"])


def extent():
    # Set up Plotly for Jupyterlab
    jupyter = 'env/bin/jupyter'
    subprocess.call([f"{jupyter}", "labextension", "install", "@jupyter-widgets/jupyterlab-manager@0.36", "--no-build"])
    subprocess.call([f"{jupyter}", "labextension", "install", "plotlywidget@0.2.1", "--no-build"])
    subprocess.call([f"{jupyter}", "labextension", "install", "@jupyterlab/plotly-extension@0.16", "--no-build"])
    subprocess.call([f"{jupyter}", "lab", "build"])
    
    print(f"{MESSAGE_COLOR} IT'S NORMAL THAT APPEARS AN ERROR ASKING FOR NODEJS. LET'S CHECK IT LISTING THE EXTENSIONS{RESET_ALL}")
    subprocess.call([f"{jupyter}", "labextension", "list"])
    print(f"{MESSAGE_COLOR} All Done{RESET_ALL}")
{% endif %}

environ()
nb()
{% if cookiecutter.project_packages == "All" %}
extent()
{% endif %}