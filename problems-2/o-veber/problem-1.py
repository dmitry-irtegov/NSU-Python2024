import unittest


def get_pythagore_triples(digit):
    return [(x, y, z) for x in range(0, digit + 1)
            for y in range(0, digit + 1)
            for z in range(0, digit + 1)
            if x ** 2 + y ** 2 == z ** 2]


class TestPythagore(unittest.TestCase):

    def test_negative_case(self):
        self.assertEqual([], get_pythagore_triples(-100))

    def test_zero_case(self):
        self.assertEqual([(0, 0, 0)], get_pythagore_triples(0))

    def test_one_case(self):
        self.assertEqual([(0, 0, 0), (0, 1, 1), (1, 0, 1)], get_pythagore_triples(1))

    def test_two_case(self):
        self.assertEqual([(0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 1), (2, 0, 2)], get_pythagore_triples(2))

    def test_five_case(self):
        self.assertEqual(
            [(0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4), (0, 5, 5), (1, 0, 1), (2, 0, 2), (3, 0, 3),
             (3, 4, 5), (4, 0, 4), (4, 3, 5), (5, 0, 5)], get_pythagore_triples(5))

    def test_ten_case(self):
        self.assertEqual(
            [(0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4), (0, 5, 5), (0, 6, 6), (0, 7, 7), (0, 8, 8),
             (0, 9, 9), (0, 10, 10), (1, 0, 1), (2, 0, 2), (3, 0, 3), (3, 4, 5), (4, 0, 4), (4, 3, 5), (5, 0, 5),
             (6, 0, 6), (6, 8, 10), (7, 0, 7), (8, 0, 8), (8, 6, 10), (9, 0, 9), (10, 0, 10)],
            get_pythagore_triples(10))


if __name__ == "__main__":
    unittest.main()
