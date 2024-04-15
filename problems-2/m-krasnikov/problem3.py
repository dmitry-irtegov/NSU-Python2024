import os
import sys


def sort_files_by_size(directory_path):
    files = []

    try:
        for filename in get_filenames(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                files.append((filename, file_size))

        files.sort(key=lambda file_info: (-file_info[1], file_info[0]))

        for file_name, file_size in files:
            print(f"{file_name}: {file_size} bytes")
    except Exception as err:
        sys.stderr.write(repr(err))


def get_filenames(directory_path):
    try:
        return os.listdir(directory_path)
    except FileNotFoundError as err:
        raise FileNotFoundError("Directory does not exist: '%s'" % directory_path, repr(err))
    except PermissionError as err:
        raise PermissionError("Permission denied: '%s'" % directory_path, repr(err))
    except OSError as err:
        raise OSError("Path error: '%s'" % directory_path, repr(err))
    except Exception as err:
        raise Exception("Get filenames error: '%s'" % directory_path, repr(err))


def is_file(file_path):
    try:
        return os.path.isfile(file_path)
    except FileNotFoundError as err:
        raise FileNotFoundError("File does not exist: '%s'" % file_path, repr(err))
    except PermissionError as err:
        raise PermissionError("Permission denied: '%s'" % file_path, repr(err))
    except OSError as err:
        raise OSError("Path '%s' does not exists or is inaccessible" % file_path, repr(err))
    except Exception as err:
        raise Exception("Is file error: '%s'" % file_path, repr(err))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python program.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        sys.stderr.write("Error: Directory does not exist.")
        sys.exit(1)

    sort_files_by_size(directory_path)
