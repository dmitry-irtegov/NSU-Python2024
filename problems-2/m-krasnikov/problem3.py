import os
import sys


def sort_files_by_size(directory_path):
    files = []

    for filename in get_filenames(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            file_size = get_file_size(file_path)
            files.append((filename, file_size))

    files.sort(key=lambda file_info: (-file_info[1], file_info[0]))

    for file_name, file_size in files:
        print(f"{file_name}: {file_size} bytes")


def get_filenames(directory_path):
    try:
        return os.listdir(directory_path)
    except FileNotFoundError:
        sys.stderr.write("Directory does not exist: '%s'" % directory_path)
    except PermissionError:
        sys.stderr.write("Permission denied: '%s'" % directory_path)
    except OSError:
        sys.stderr.write("Path error: '%s'" % directory_path)


def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except OSError:
        sys.stderr.write("Error while getting size of file '%s'" % file_path)


def is_file(file_path):
    try:
        return os.path.isfile(file_path)
    except FileNotFoundError:
        sys.stderr.write("File does not exist: '%s'" % file_path)
    except PermissionError:
        sys.stderr.write("Permission denied: '%s'" % file_path)
    except OSError:
        sys.stderr.write("Path '%s' does not exists or is inaccessible" % file_path)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python program.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        sys.stderr.write("Error: Directory does not exist.")
        sys.exit(1)

    sort_files_by_size(directory_path)
