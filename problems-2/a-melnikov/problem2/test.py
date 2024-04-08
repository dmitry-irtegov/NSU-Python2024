from main import convert
import os
import unittest


class ConverterTestCase(unittest.TestCase):
    def test(self):
        res_name: str = "resources/eng-lat_dict.txt"
        convert("resources/lat-eng_dict.txt", res_name)
        with open(res_name, "r") as res_file, open(
            "resources/expected.txt", "r"
        ) as expected:
            self.assertEqual(res_file.readlines(), expected.readlines())
        os.remove(res_name)


if __name__ == "__main__":
    unittest.main()
