# problems-2/assignment-1
import unittest


def pythagorean_threes(n: int):
    return [(x, y, z) for x in range(1, n)
            for y in range(x, n)
            for z in range(y, n)
            if x ** 2 + y ** 2 == z ** 2]


class PythagoreanThrees(unittest.TestCase):
    def test_init(self):
        self.assertEqual([(3, 4, 5), (5, 12, 13), (6, 8, 10)], pythagorean_threes(15))

    def test_zero(self):
        self.assertEqual([], pythagorean_threes(0))

    def test_negative_number(self):
        self.assertEqual([], pythagorean_threes(-3))

    def test_pythagorean_triplets(self):
        triplets = pythagorean_threes(100)
        for triplet in triplets:
            a, b, c = triplet
            self.assertTrue(a ** 2 + b ** 2 == c ** 2)
        self.assertEqual(len(triplets), len(set(triplets)))


if __name__ == '__main__':
    unittest.main()
