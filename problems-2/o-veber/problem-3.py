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


if __name__ == "__main__":
    thrown_stats_exceptions = []
    try:
        parser = ArgumentParser()
        parser.add_argument("directory", help="Absolute path for target directory to list files in")
        directory_path = parser.parse_args().directory
        elements_in_dir = get_dir_elements()
        file_stats = {}
        for element in elements_in_dir:
            element_absolute_path = join(directory_path, element)
            try:
                if isfile(element_absolute_path):
                    file_stats[element] = stat(path=element_absolute_path).st_size
            except OSError as os_error:
                os_error.strerror = f"Trying to stat file {element} but catch exception:" + os_error.strerror
                thrown_stats_exceptions.append(os_error)
                file_stats[element] = -1
            except BaseException as e:
                e.args = (f"Trying to stat file {element}, but caught exception", *e.args)
                thrown_stats_exceptions.append(e)
                file_stats[element] = -1
        for file in sorted(file_stats.items(), key=lambda x: x[1], reverse=True):
            print(f'File with name=\"{file[0]}\" and size={file[1]}')
        if len(thrown_stats_exceptions) > 0:
            print('Caught exception while trying to stat files in directory:', file=stderr)
        for e in thrown_stats_exceptions:
            print(e, file=stderr)
    except BaseException as e:
        print("Caught unhandled exception while execution:", e, file=stderr)
