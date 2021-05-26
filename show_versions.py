#!/usr/bin/python3
from getpass import getuser
import glob
import sys

global version


def get_list_of_python_scripts_in_dir() -> list[str]:
    list_of_files_with_dir = glob.glob("/home/user/commands/*.py")
    for idx, path in enumerate(list_of_files_with_dir, 0):
        filename_without_extension = path.rsplit("/", 1)[1][:-3]
        list_of_files_with_dir[idx] = filename_without_extension
    return list_of_files_with_dir


def get_version(filename_list):
    for filename in filename_list:
        exec(f"import {filename}")
        exec(f"global version; version = {filename}.version")
        if callable(version):
            exec(f"global version; version = {filename}.version()")
            sys.stdout.write(f"Version of {filename}.py retrieved from Function:\033[1m {version} \033[0m\n")
        else:
            sys.stdout.write(f"Version of {filename}.py retrieved from Variable:\033[1m {version}\033[0m\n")


if __name__ == '__main__':
    user = getuser()
    sys.path.insert(0, f"/home/{user}/commands/")   # Mac: change "home" to "Users"
    files_in_dir = get_list_of_python_scripts_in_dir()
    get_version(files_in_dir)
