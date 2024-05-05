import unittest

from tr import Tr


class TestTranslateLine(unittest.TestCase):

    def test_translate_line_no_replacement(self):
        self.translator = Tr("aeiou", "12345", "bsz")
        line = ":DDDDDD"
        result = self.translator.translate_line(line)
        self.assertEqual(result, line)

    def test_translate_line_with_replacement(self):
        self.translator = Tr("aeiou", "12345")
        line = "Hello World"
        expected_result = "H2ll4 W4rld"
        result = self.translator.translate_line(line)
        self.assertEqual(result, expected_result)

    def test_translate_line_with_deletion(self):
        self.translator = Tr("", "", "aeiou")
        line = "Hello World"
        expected_result = "Hll Wrld"
        result = self.translator.translate_line(line)
        self.assertEqual(result, expected_result)

    def test_translate_line_with_both_replacement_and_deletion(self):
        self.translator = Tr("aeiou", "12345", "l")
        line = "Hello World"
        expected_result = "H24 W4rd"
        result = self.translator.translate_line(line)
        self.assertEqual(result, expected_result)

    def test_repeated_chars(self):
        with self.assertRaises(ValueError):
            self.tr = Tr("dvdv", "abcd")

    def test_different_size(self):
        with self.assertRaises(ValueError):
            self.tr = Tr("abcd", "xyz")


if __name__ == '__main__':
    unittest.main()
