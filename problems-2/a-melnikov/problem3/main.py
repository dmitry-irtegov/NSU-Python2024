import os
import sys
from typing import TextIO, Tuple


def list_sorted_dir(dir_path: str, errfile: TextIO) -> None:
    def construct_filepath(filename: str) -> str:
        return os.path.join(dir_path, filename)

    try:
        elements: list[str] = os.listdir(dir_path)
    except BaseException as e:
        raise type(e)(f"Tried to list a directory '{dir_path}': {e}") from e

    files: list[Tuple[int, str]] = []
    for element in elements:
        try:
            filepath: str = construct_filepath(element)
            size = os.stat(filepath).st_size
            if os.path.isfile(filepath):
                files.append((size, element))
        except BaseException as e:
            print(f"File '{element}' is not accessible. {e}", file=errfile)

    files.sort(key=lambda file: file[0], reverse=True)

    for filename in files:
        print(filename[1], filename[0])


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
