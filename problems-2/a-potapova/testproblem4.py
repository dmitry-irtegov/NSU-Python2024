import unittest
from problem4 import search_sequence


class TestSearchSequence(unittest.TestCase):
    def test_search_sequence(self):
        indexes = search_sequence("123")
        self.assertEqual(len(indexes), 4185)
        self.assertEqual(indexes[0], 1923)
        self.assertEqual(indexes[1], 2937)
        self.assertEqual(indexes[2], 2975)
        indexes = search_sequence("1415")
        self.assertEqual(len(indexes), 424)
        self.assertEqual(indexes[0], 0)
        self.assertEqual(indexes[1], 6954)
        self.assertEqual(indexes[2], 29135)


if __name__ == '__main__':
    unittest.main()
