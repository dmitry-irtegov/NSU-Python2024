from main import list_sorted_dir
import unittest
from io import StringIO
import sys


class TestListSortedDir(unittest.TestCase):
    held_output: StringIO

    def setUp(self) -> None:
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_normal_dir(self):
        list_sorted_dir("resources/straight_dir")
        self.held_output.seek(0)
        output: str = self.held_output.read().strip()
        expected: str = """straight_file2.txt 68
straight_file4.txt 55
straight_file.txt 25
straight_file3.txt 0"""
        self.assertEqual(expected, output)

    def test_protected_dir(self):
        def method():
            list_sorted_dir("resources/protected_dir")

        self.assertRaises(PermissionError, method)

    def test_mixed_dir(self):
        list_sorted_dir("resources/mixed_dir")
        self.held_output.seek(0)
        output: str = self.held_output.read().strip()
        expected: str = """abc.txt 0
def.txt 0"""
        self.assertEqual(expected, output)

    def test_inaccessible_dir(self):
        list_sorted_dir("resources/inaccessible_dir")
        self.held_output.seek(0)
        output: str = self.held_output.read().strip()
        expected: str = ""
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
