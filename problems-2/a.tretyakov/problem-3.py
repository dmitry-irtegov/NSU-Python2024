import sys
from os.path import isfile, isdir, join
from os import listdir, stat


def get_file_size(file_path):
    return stat(file_path).st_size


def list_files_by_size(directory):
    files = [file for file in listdir(directory) if isfile(join(directory, file))]
    files.sort(key=lambda x: (-get_file_size(join(directory, x)), x))
    return files


def main():
    if len(sys.argv) != 2:
        print("Usage: python problem-3.py <directory>")
        return

    directory = sys.argv[1]
    if not isdir(directory):
        print("Error: Directory not found.")
        return

    files = list_files_by_size(directory)
    for file in files:
        file_path = join(directory, file)
        size = get_file_size(file_path)
        print(f"{file}: {size} bytes")


if __name__ == "__main__":
    main()
