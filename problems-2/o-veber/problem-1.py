import unittest


def get_pithagor_triples(digit):
    return [(x, y, z) for x in range(0, digit + 1)
            for y in range(0, digit + 1)
            for z in range(0, digit + 1)
            if x ** 2 + y ** 2 == z ** 2]


class TestSong(unittest.TestCase):
    def test_negative_case(self):
        self.assertEqual([], get_pithagor_triples(-100))

    def test_zero_case(self):
        self.assertEqual([(0, 0, 0)], get_pithagor_triples(0))

    def test_one_case(self):
        self.assertEqual([(0, 0, 0), (0, 1, 1), (1, 0, 1)], get_pithagor_triples(1))

    def test_two_case(self):
        self.assertEqual([(0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 1), (2, 0, 2)], get_pithagor_triples(2))


if __name__ == "__main__":
    unittest.main()
