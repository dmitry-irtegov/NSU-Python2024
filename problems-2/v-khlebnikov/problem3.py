import argparse
import os
import sys


def get_file_size(name):
    try:
        return os.stat(name).st_size
    except FileNotFoundError as e:
        return -1


def bytes_to_string(b):
    if not isinstance(b, (int, float)):
        print("Argument must be a number", file=sys.stderr)
        return ""
    if b < 0:
        return "-1"

    size_unit = ['B', 'KB', 'MB', 'GB', 'TB']
    unit = 0
    while b >= 1024 and unit < len(size_unit) - 1:
        b = b / 1024
        unit = unit + 1
    return "{:8.1f}".format(b) + " " + size_unit[unit]


def print_files(path):
    try:
        filenames = os.listdir(path)
        files = {}
        longest_string_size = 0

        for f in filenames:
            longest_string_size = max(longest_string_size, len(f))
            p = os.path.join(path, f)
            if os.path.isfile(p):
                files[f] = get_file_size(p)
        files = sorted(files.items(), key=lambda x: x[1], reverse=True)
        for f in files:
            print('{:{val}}'.format(f[0], val=longest_string_size) + " size: " + bytes_to_string(f[1]))
    except FileNotFoundError as e:
        print("Trying to get directories in current path, but path doesn't exist: " + e.filename, file=sys.stderr)
        exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='directory path')
    args = parser.parse_args()

    print_files(args.path)


if __name__ == '__main__':
    main()
