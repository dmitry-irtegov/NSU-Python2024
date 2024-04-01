from os import listdir, stat
from os.path import isfile, join
from argparse import ArgumentParser
from sys import stderr


def get_dir_elements():
    try:
        return listdir(directory_path)
    except OSError as os_error:
        os_error.strerror = "Trying to list files, but caught exception\n" + os_error.strerror
        raise os_error
    except BaseException as err:
        err.args = ("Trying to list files, but caught exception", *err.args)
        raise err


def get_file_stat():
    try:
        return stat(path=element_absolute_path).st_size
    except Exception:
        return -1


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
        print("Caught exception while execution:", e, file=stderr)
