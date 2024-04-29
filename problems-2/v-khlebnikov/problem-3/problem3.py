import argparse
import humanize
import os
import sys


def get_file_size(name):
    try:
        return os.stat(name).st_size
    except BaseException as e:
        print("Cannot access " + name + ": Permission denied: ", e, file=sys.stderr)
        return 0


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
            file_size_string = "{:8}".format(humanize.naturalsize(f[1]))
            print('{:{val}}'.format(f[0], val=longest_string_size) + " size: " + file_size_string)
    except BaseException as e:
        print("Caught unhandled exception while execution:", e, file=sys.stderr)
        exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='directory path')
    args = parser.parse_args()

    print_files(args.path)


if __name__ == '__main__':
    main()
