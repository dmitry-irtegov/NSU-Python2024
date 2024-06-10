import unittest

import cipher.table.entity.frequencydata as frequency
from cipher.table.entity.text import TableText


class TestFrequency(unittest.TestCase):
    def test_frequency(self):
        text = TableText("text")
        expected = {'a': 0.0,
                    'b': 0.0,
                    'c': 0.0,
                    'd': 0.0,
                    'e': 0.25,
                    'f': 0.0,
                    'g': 0.0,
                    'h': 0.0,
                    'i': 0.0,
                    'j': 0.0,
                    'k': 0.0,
                    'l': 0.0,
                    'm': 0.0,
                    'n': 0.0,
                    'o': 0.0,
                    'p': 0.0,
                    'q': 0.0,
                    'r': 0.0,
                    's': 0.0,
                    't': 0.5,
                    'u': 0.0,
                    'v': 0.0,
                    'w': 0.0,
                    'x': 0.25,
                    'y': 0.0,
                    'z': 0.0}
        fd = frequency.text_to_frequencies(text)
        self.assertEqual(fd, expected)
