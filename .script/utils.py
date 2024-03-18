import configparser
import os
import subprocess

import yaml

def get_directories(root='.', depth=1, current_depth=0):
    directories = []

    if current_depth > depth:
        return directories

    for entry in os.listdir(root):
        full_path = os.path.join(root, entry)
        relative_path = os.path.relpath(full_path, start=os.getcwd())
        if os.path.isdir(full_path):
            if current_depth == depth:
                directories.append(relative_path)
            if not relative_path.startswith("."):
                subdirectories = get_directories(full_path, depth, current_depth + 1)
                directories.extend(subdirectories)

    return directories


def read_ctf_config(root=os.getcwd()):
    config_file = os.path.join(root, ".ctf/config")
    with open(config_file, "r") as fp:
        config = configparser.ConfigParser()
        config.read_file(fp)
    return config

def save_ctf_config(config: configparser.ConfigParser, root=os.getcwd()):
    config_file = os.path.join(root, ".ctf/config")
    with open(config_file, "w") as fp:
        config.write(fp)

async def run_script(chall_dir, script_key):
    print(f"Processing directory: {chall_dir}")
    with open(os.path.join(chall_dir, "challenge.yaml"), "r") as fp:
        chall_conf: dict = yaml.load(fp, Loader=yaml.Loader)
    script = chall_conf.get("script")
    if script:
        subprocess.run(script[script_key], shell=True, cwd=chall_dir)
