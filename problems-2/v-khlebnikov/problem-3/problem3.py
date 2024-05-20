import argparse
import humanize
import os
import sys


def get_listdir(path):
    try:
        return os.listdir(path)
    except OSError as e:
        e.strerror = "Cannot get list of files in '" + path + "': " + e.strerror
        raise e
    except BaseException as e:
        e.args = ("Cannot get list of files in '" + path + "'", *e.args)
        raise e


def get_file_size(name):
    try:
        return os.stat(name).st_size
    except OSError as e:
        e.strerror = "Cannot access file'" + name + "': " + e.strerror
        raise e
    except BaseException as e:
        e.args = ("Cannot access file'" + name + "'", *e.args)
        raise e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='directory path')
    args = parser.parse_args()

    try:
        filenames = get_listdir(args.path)
    except BaseException as e:
        print("Trying to get list of files, but: ", e, file=sys.stderr)
        exit(1)

    files = {}
    longest_string_size = 0

    for f in filenames:
        longest_string_size = max(longest_string_size, len(f))
        file_path = os.path.join(args.path, f)

        try:
            if os.path.isfile(file_path):
                files[f] = get_file_size(file_path)
        except BaseException as e:
            print("Trying to get size of file '" + file_path + "' but: ", e, file=sys.stderr)

    files = sorted(files.items(), key=lambda x: x[1], reverse=True)
    for f in files:
        file_size_string = "{:8}".format(humanize.naturalsize(f[1]))
        print('{:{val}}'.format(f[0], val=longest_string_size) + " size: " + file_size_string)
