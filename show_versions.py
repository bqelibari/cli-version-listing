#!/usr/bin/python3
from getpass import getuser
from glob import glob
from sys import path, stdout
from os import chdir

global version


def get_list_of_python_scripts_in_dir() -> list[str]:
    chdir("/home/user/commands/")
    list_of_files_with_dir = glob("*.py")
    for idx, file in enumerate(list_of_files_with_dir, 0):
        filename_without_extension = file[:-3]
        list_of_files_with_dir[idx] = filename_without_extension
    return list_of_files_with_dir


def get_version(filename_list):
    for filename in filename_list:
        exec(f"import {filename}")
        exec(f"global version; version = {filename}.version")
        if callable(version):
            exec(f"global version; version = {filename}.version()")
            stdout.write(f"Version of {filename}.py retrieved from Function: {version}\n")
        else:
            stdout.write(f"Version of {filename}.py retrieved from Variable: {version}\n")


if __name__ == '__main__':
    user = getuser()
    path.insert(0, f"/home/{user}/commands/")   # Mac: change "home" to "Users"
    files_in_dir = get_list_of_python_scripts_in_dir()
    get_version(files_in_dir)
