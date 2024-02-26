import sys
import os


def get_files(directory_path: str):
    filenames = os.listdir(directory_path)
    directory_files = [None] * len(filenames)
    for i, filename in enumerate(filenames):
        size = os.stat(directory_path + '/' + filename).st_size
        directory_files[i] = (filename, size)
    directory_files.sort(key=lambda x: (-x[1], x[0]))
    return directory_files


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Incorrect number of arguments')
        path = sys.argv[1]
        print(f"current directory: {path}")
        files = get_files(path)
        print(f"{'NAME':<50}  {'SIZE (in bytes)':<4}")
        for file in files:
            print(f"{file[0]:<50}  {file[1]:<4}")
    except (ValueError, NotADirectoryError) as e:
        print(e)
