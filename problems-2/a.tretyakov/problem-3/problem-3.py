from argparse import ArgumentParser
from os import listdir, stat
from os.path import join
from sys import stderr


def get_file_size(path):
    try:
        return stat(path).st_size
    except PermissionError as e:
        print(f"Cannot retrieve information about file {path}", e, file=stderr)


def list_files_by_size(directory):
    directory_files = get_files(directory)
    retrieved_files = [inner_file for inner_file in directory_files]
    retrieved_files.sort(key=lambda x: (-get_file_size(join(directory, x)), x))
    return retrieved_files


def get_files(path):
    try:
        return listdir(path)
    except Exception as e:
        print(f"Cannot open catalog {path} : {e}", file=stderr)
    return {}


if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        parser.add_argument("dir", help="Lists file size in directory. Note: gets ABSOLUTE path of the directory")
        dir_path = parser.parse_args().dir

        files = list_files_by_size(dir_path)

        for file in files:
            file_path = join(dir_path, file)
            size = get_file_size(file_path)
            print(f"{file}: {size} bytes")

    except BaseException as base_exception:
        print("Unhandled exception", base_exception, file=stderr)
