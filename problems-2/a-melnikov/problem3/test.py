from main import list_sorted_dir
import unittest
from io import StringIO
import sys


class TestListSortedDir(unittest.TestCase):
    held_output: StringIO
    errlog: StringIO

    def setUp(self) -> None:
        self.held_output = StringIO()
        self.errlog = StringIO()
        sys.stdout = self.held_output

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_regular_dir(self):
        list_sorted_dir("resources/regular_dir", self.errlog)

        self.errlog.seek(0)
        output_errlog = self.errlog.read().strip()
        expected_errlog = (
            "File 'symlink.txt' is not accessible. [Errno 2] No such file or directory: 'resources/regular_dir/symlink.txt'"
        )
        self.assertEqual(expected_errlog, output_errlog)

        self.held_output.seek(0)
        output = self.held_output.read().strip()
        expected_output = """big_file.txt 42
middle_file.txt 26
small_file.txt 11
write_only_file.txt 0
regular_empty_file.txt 0
exec_only_file.txt 0
read_only_file.txt 0
protected_file.txt 0"""
        self.assertEqual(expected_output, output)

    def test_exec_only_dir(self) -> None:
        self.assertRaises(
            PermissionError,
            lambda: list_sorted_dir("resources/exec_only_dir", self.errlog),
        )

        self.errlog.seek(0)
        output_errlog: str = self.errlog.read().strip()
        expected_errlog: str = ""
        self.assertEqual(expected_errlog, output_errlog)

        self.held_output.seek(0)
        output: str = self.held_output.read().strip()
        expected_output: str = ""
        self.assertEqual(expected_output, output)

    def test_read_only_dir(self) -> None:
        list_sorted_dir("resources/read_only_dir", self.errlog)

        self.errlog.seek(0)
        output_errlog: str = self.errlog.read().strip()
        expected_errlog: str = """File 'small_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/small_file.txt'
File 'write_only_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/write_only_file.txt'
File 'symlink.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/symlink.txt'
File 'regular_empty_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/regular_empty_file.txt'
File 'middle_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/middle_file.txt'
File 'exec_only_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/exec_only_file.txt'
File 'read_only_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/read_only_file.txt'
File 'protected_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/protected_file.txt'
File 'big_file.txt' is not accessible. [Errno 13] Permission denied: 'resources/read_only_dir/big_file.txt'"""
        self.assertEqual(expected_errlog, output_errlog)

        self.held_output.seek(0)
        output: str = self.held_output.read().strip()
        expected_output: str = ""
        self.assertEqual(expected_output, output)

    def test_protected_dir(self) -> None:
        self.assertRaises(
            PermissionError,
            lambda: list_sorted_dir("resources/exec_only_dir", self.errlog),
        )

        self.errlog.seek(0)
        output_errlog: str = self.errlog.read().strip()
        expected_errlog: str = ""
        self.assertEqual(expected_errlog, output_errlog)

        self.held_output.seek(0)
        output: str = self.held_output.read().strip()
        expected_output: str = ""
        self.assertEqual(expected_output, output)


if __name__ == "__main__":
    unittest.main()
