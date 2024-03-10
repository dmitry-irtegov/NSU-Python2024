import argparse
import os
import sys


def get_file_size(name):
    try:
        return os.stat(name).st_size
    except FileNotFoundError as e:
        print("File \"" + e.filename + "\" doesn't exist", file=sys.stderr)


def bytes_to_string(Bytes):
    if not isinstance(Bytes, (int, float)):
        raise TypeError("Argument must be a number")
    if Bytes < 0:
        raise ValueError("Argument must be greater or equals to zero")
    size_unit = ['B', 'KB', 'MB', 'GB', 'TB']
    unit = 0
    while Bytes >= 1024 and unit < len(size_unit) - 1:
        Bytes = Bytes / 1024
        unit = unit + 1
    return "{:8.1f}".format(Bytes) + " " + size_unit[unit]


def print_files(path):
    try:
        filenames = os.listdir(path)
        files = {}
        longest_string_size = 0
        o = '{'
        c = '}'
        for f in filenames:
            longest_string_size = max(longest_string_size, len(f))
            p = os.path.join(path, f)
            if os.path.isfile(p):
                files[f] = get_file_size(p)
        files = sorted(files.items(), key=lambda x: x[1], reverse=True)
        for f in files:
            print(f'{o}:{longest_string_size}{c}'.format(f[0]) + " size: " + bytes_to_string(f[1]))
    except FileNotFoundError as e:
        print("Current path doesn't exist: " + e.filename, file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='directory path')
    args = parser.parse_args()

    print_files(args.path)


if __name__ == '__main__':
    main()
