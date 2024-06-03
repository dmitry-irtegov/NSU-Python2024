import os
import sys
import unittest
import tempfile
from contextlib import contextmanager
from io import StringIO


@contextmanager
def capture_output():
    old_stdout, old_stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = StringIO(), StringIO()
    try:
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr


def list_files_sorted_by_size(directory):
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.", file=sys.stderr)
        return
    except PermissionError:
        print(f"Error: Cannot read the directory '{directory}' due to insufficient permissions.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Error: An unexpected error occurred while listing files in '{directory}': {e}", file=sys.stderr)
        return

    files_with_sizes = []
    for f in files:
        file_path = os.path.join(directory, f)
        try:
            file_size = os.stat(file_path).st_size
            files_with_sizes.append((f, file_size))
        except Exception as e:
            print(f"Warning: An error occurred while getting information about '{file_path}': {e}", file=sys.stderr)

    files_with_sizes.sort(key=lambda x: (-x[1], x[0]))
    for file, size in files_with_sizes:
        print(f"{file}: {size} bytes")


class TestListFilesSortedBySize(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()

    def test_directory_not_exists(self):
        with capture_output() as (out, err):
            list_files_sorted_by_size('non_existing_directory')
        self.assertIn("Error: The directory 'non_existing_directory' does not exist.", err.getvalue())

    def test_permission_error(self):
        if os.name == 'nt':
            print("Permission error test is skipped on Windows due to limitations in setting directory permissions.")
            return

        os.chmod(self.test_dir.name, 0o000)
        with capture_output() as (out, err):
            list_files_sorted_by_size(self.test_dir.name)
        self.assertIn(f"Error: Cannot read the directory '{self.test_dir.name}' due to insufficient permissions.",
                      err.getvalue())
        os.chmod(self.test_dir.name, 0o700)

    def test_list_files(self):
        file1_path = os.path.join(self.test_dir.name, 'file1.txt')
        file2_path = os.path.join(self.test_dir.name, 'file2.txt')
        with open(file1_path, 'w') as file1:
            file1.write('A' * 50)
        with open(file2_path, 'w') as file2:
            file2.write('B' * 100)

        with capture_output() as (out, err):
            list_files_sorted_by_size(self.test_dir.name)
        self.assertIn("file2.txt: 100 bytes", out.getvalue())
        self.assertIn("file1.txt: 50 bytes", out.getvalue())


if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
        list_files_sorted_by_size(directory_path)
    else:
        unittest.main(argv=[sys.argv[0]], exit=False)
