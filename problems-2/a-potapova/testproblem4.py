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

    def test_search_sequence_at_last_block(self):
        indexes = search_sequence("1350")
        self.assertEqual(len(indexes), 429)
        self.assertEqual(indexes[428], 4194299)

    def test_search_big_sequence(self):
        indexes = search_sequence("17450284102701938521105559644622948954930381964428810975665933446128475648233786783")
        self.assertEqual(len(indexes), 1)
        self.assertEqual(indexes[0], 154)
        indexes = search_sequence(
            "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066")
        self.assertEqual(len(indexes), 1)
        self.assertEqual(indexes[0], 0)


if __name__ == '__main__':
    unittest.main()
