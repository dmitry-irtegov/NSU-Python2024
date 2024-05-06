import argparse
import humanize
import os
import sys


def get_listdir(path):
    try:
        return os.listdir(path)
    except PermissionError as e:
        e.strerror = "Cannot get list of files in '" + path + "': permission denied: " + e.strerror
        raise e
    except FileNotFoundError as e:
        e.strerror = "Cannot get list of files in '" + path + "': directory wasn't found: " + e.strerror
        raise e
    except NotADirectoryError as e:
        e.strerror = "Cannot get list of files in '" + path + "': path is not a directory: " + e.strerror
        raise e
    except OSError  as e:
        e.strerror = "Cannot get list of files in '" + path + "': " + e.strerror
        raise e


def get_file_size(name):
    try:
        return os.stat(name).st_size
    except PermissionError as e:
        e.strerror = "Cannot access " + name + ": Permission denied: " + e.strerror
        raise e
    except FileNotFoundError as e:
        e.strerror = "Cannot access " + name + ": File not found: " + e.strerror
        raise e
    except OSError as e:
        e.strerror = "Cannot access " + name + ":  " + e.strerror
        raise e
    
def sorted_filtered(items):
    items = filter(lambda x: x[1] != -1, items)
    return sorted(items, key=lambda x: x[1], reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='directory path')
    args = parser.parse_args()

    try:
        filenames = get_listdir(args.path)
    except BaseException as e:
        print("Trying to get list of files, but: " + e.strerror, file=sys.stderr)
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
            print("Trying to get size of file '" + file_path + "' but: " + e.strerror, file=sys.stderr)
            files[f] = -1
    
    files = sorted_filtered(files.items())
    for f in files:
        file_size_string = "{:8}".format(humanize.naturalsize(f[1]))
        print('{:{val}}'.format(f[0], val=longest_string_size) + " size: " + file_size_string)


if __name__ == '__main__':
    main()
