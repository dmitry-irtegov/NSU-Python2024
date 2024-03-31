import argparse
import sys
import os


def init_parser():
    parser = argparse.ArgumentParser(description='Display files from a given directory.')
    parser.add_argument('path', type=str,
                        help='directory path')
    return parser


def get_files(directory_path: str) -> list:
    filenames = os.listdir(directory_path)
    directory_files = [None] * len(filenames)
    for i, filename in enumerate(filenames):
        size = -1
        try:
            size = os.stat(directory_path + '/' + filename).st_size
        except OSError:
            sys.stderr.write(f"Error while getting file size: {directory_path + '/' + filename}\n")
        directory_files[i] = (filename, size)
    directory_files.sort(key=lambda x: (-x[1], x[0]))
    return directory_files


if __name__ == '__main__':
    args = init_parser().parse_args()
    try:
        files = get_files(args.path)
    except Exception as e:
        sys.stderr.write(f"Error while getting files info: {str(e)}")
        exit(1)
    print(f"Current directory: {args.path}")
    print(f"{'NAME':<50}  {'SIZE (in bytes)':<4}")
    for file in files:
        filename, size = file
        size = str(size) if size != -1 else "None"
        print(f"{filename:<50}  {size:<4}")
