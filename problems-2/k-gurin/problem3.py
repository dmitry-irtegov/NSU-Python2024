import os
import argparse
import sys


def parse() -> str:
    parser = argparse.ArgumentParser(description='Show sorted files in directory')
    parser.add_argument('path', type=str, help='Directory path')
    args = parser.parse_args()
    return args.path


def get_files(path: str) -> list:
    files = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            try:
                file_size = os.stat(file_path).st_size
                files.append((file, file_size))
            except Exception as e:
                print(f"Error while getting file info for '{file}': {e}")

    return sorted(files, key=lambda item: (-item[1], item[0]))


if __name__ == '__main__':
    path_to_dir = parse()
    try:
        files_list = get_files(path_to_dir)
        for f in files_list:
            print(f"{f[0]} \t {f[1]}")
    except Exception as e:
        sys.stderr.write(f"Error while getting files in \"{path_to_dir}\": {str(e)}\n")
