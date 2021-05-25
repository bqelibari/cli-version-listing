#!/usr/bin/python3
import glob
import os
import sys
from typing import Any


def get_list_of_python_scripts_in_dir() -> list[str]:
    list_of_files_with_dir = glob.glob("/home/user/commands/*.py", recursive=True)
    for idx, path in enumerate(list_of_files_with_dir, 0):
        filename: str = path.rsplit("/", 1)[1]
        list_of_files_with_dir[idx] = filename
    return list_of_files_with_dir


def open_python_files_and_get_versions(list_of_files: list) -> list[tuple[Any, str]]:
    filename_version_list: list[tuple[Any, str]] = []
    for file in list_of_files:
        with open(file) as current_file:
            list_of_lines_in_current_file: list[str] = current_file.readlines()
            version: str = _search_for_version_in_current_file(list_of_lines_in_current_file)
        if version is not None:
            filename_version_list.append((file, version))
    return filename_version_list


def _search_for_version_in_current_file(list_of_lines: list[str]) -> str:
    for index, line in enumerate(list_of_lines, 0):
        line_without_newline: str = line[0:-1]
        if "version()" in line.lower():
            return _loop_until_return(list_of_lines, index)
        elif "version" in line.lower():
            return line_without_newline


def _loop_until_return(list_of_lines: list[str], idx: int) -> str:
    for element in list_of_lines[idx:]:
        if "return" in element:
            split_return_statement = element.split(" ")
            return "Return Value = " + split_return_statement[1][0:-1]


def format_and_print_output():
    sys.stdout.write("File: Version\n\n")
    for filename, version in list_of_name_version_tuples:
        sys.stdout.write(f"{filename}:  {version}\n")


if __name__ == '__main__':
    os.chdir("/home/user/commands/")
    files_in_dir = get_list_of_python_scripts_in_dir()
    list_of_name_version_tuples = open_python_files_and_get_versions(files_in_dir)
    format_and_print_output()
