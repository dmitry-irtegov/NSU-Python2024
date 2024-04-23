import os
import sys
from typing import TextIO


def list_sorted_dir(dir_path: str, errfile: TextIO) -> None:
    def construct_filepath(filename: str) -> str:
        return os.path.join(dir_path, filename)

    try:
        elements: list[str] = os.listdir(dir_path)
    except BaseException as e:
        raise type(e)(f"Tried to list a directory '{dir_path}': {e}") from e

    files: list[str] = []
    for element in elements:
        try:
            filepath: str = construct_filepath(element)
            os.stat(filepath)
            if os.path.isfile(filepath):
                files.append(element)
        except BaseException:
            print(f"File '{element}' is not accessible", file=errfile)

    def get_file_size(filename: str) -> int:
        return os.stat(construct_filepath(filename)).st_size

    files.sort(key=get_file_size, reverse=True)

    for filename in files:
        print(filename, os.stat(construct_filepath(filename)).st_size)


def main(args: list[str]) -> int:
    if len(args) != 2:
        print("You must specify single directory to search in.", file=sys.stderr)
        return -1

    try:
        list_sorted_dir(args[1], sys.stderr)
    except BaseException as e:
        print(e, file=sys.stderr)
        return -1
    return 0


if __name__ == "__main__":
    main(sys.argv)
