import argparse
import humanize
import os
import sys


def get_listdir(path):
    try:
        return os.listdir(path)
    except PermissionError as e:
        raise PermissionError("Cannot get list of files in '" + path + "': permission denied: " + e)
    except FileNotFoundError as e:
        raise FileNotFoundError("Cannot get list of files in '" + path + "': directory wasn't found: " + e)
    except NotADirectoryError as e:
        raise NotADirectoryError("Cannot get list of files in '" + path + "': path is not a directory: " + e)
    except OSError  as e:
        raise OSError("Cannot get list of files in '" + path + "': " + e)


def get_file_size(name):
    try:
        return os.stat(name).st_size
    except PermissionError as e:
        raise PermissionError("Cannot access " + name + ": Permission denied: " + e)
    except FileNotFoundError as e:
        raise FileNotFoundError("Cannot access " + name + ": File not found: " + e)
    except OSError as e:
        raise OSError("Cannot access " + name + ": " + e)


def print_files(path):
    try:
        filenames = get_listdir(path)
    except BaseException as e:
        print("Trying to get list of files, but:" + e, file=sys.stderr)
        exit(1)

    files = {}
    longest_string_size = 0

    for f in filenames:
        longest_string_size = max(longest_string_size, len(f))
        file_path = os.path.join(path, f)
        try:
            if os.path.isfile(file_path):
                files[f] = get_file_size(file_path)
        except BaseException as e:
            print("Trying to get size of file '" + file_path + "' but: " + e, file=sys.stderr)
            files[f] = -1
                    
    files = sorted(files.items(), key=lambda x: x[1], reverse=True)
    for f in files:
        file_size_string = "{:8}".format(humanize.naturalsize(f[1]))
        print('{:{val}}'.format(f[0], val=longest_string_size) + " size: " + file_size_string)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='directory path')
    args = parser.parse_args()

    print_files(args.path)


if __name__ == '__main__':
    main()
