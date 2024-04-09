import os
import argparse
import sys


def parse() -> str:
    parser = argparse.ArgumentParser(description='Show sorted files in directory')
    parser.add_argument('path', type=str, help='Directory path')
    args = parser.parse_args()
    return args.path


def get_files(path: str) -> list:
    try:
        files = [
            (file, os.stat(os.path.join(path, file)).st_size)
            for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file))
        ]
        return sorted(files, key=lambda item: (-item[1], item[0]))
    except OSError:
        sys.stderr.write("Error while reading files")


if __name__ == '__main__':
    path_to_dir = parse()
    files_list = get_files(path_to_dir)
    for f in files_list:
        print(f[0], "\t", f[1])
