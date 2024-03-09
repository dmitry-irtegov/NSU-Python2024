from os import listdir, stat
from os.path import isfile, join
from argparse import ArgumentParser
from sys import stderr


def get_dir_elements():
    try:
        return listdir(directory_path)
    except NotADirectoryError:
        print(f"Trying to list files in directory with path {directory_path}, but found a file", file=stderr)
    except FileNotFoundError:
        print(f"Trying to open directory with path {directory_path}, but not found one with such name", file=stderr)
    except PermissionError:
        print(f"Trying to list files in directory with path {directory_path}, but does not have persmission to do this",
              file=stderr)
    return {}


def get_file_stat():
    try:
        return stat(path=element_absolute_path).st_size
    except PermissionError:
        print(f'Trying to stat information about file with path {element_absolute_path}, but dont have permission',
              file=stderr)


if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        parser.add_argument("directory", help="Absolute path for target directory to list files in")
        directory_path = parser.parse_args().directory
        elements_in_dir = get_dir_elements()
        file_stats = {}
        for element in elements_in_dir:
            element_absolute_path = join(directory_path, element)
            if isfile(element_absolute_path):
                file_stats[element] = get_file_stat()
        for file in sorted(file_stats.items(), key=lambda x: x[1], reverse=True):
            print(f'File with name=\"{file[0]}\" and size={file[1]}')
    except BaseException as e:
        print("Unexpected exception", e, file=stderr)
