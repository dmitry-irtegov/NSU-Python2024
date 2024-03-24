import unittest
from math import sqrt


def generate_pythagorean_triplets(number):
    return [
        [x, y, sqrt(x ** 2 + y ** 2)]
        for x in range(1, number + 1)
        for y in range(x, number + 1)
        if sqrt(x ** 2 + y ** 2) <= number and sqrt(x ** 2 + y ** 2) % 1 == 0
    ]


class TestPythagoreanTripletsGenerator(unittest.TestCase):

    def test(self):
        self.assertEqual(generate_pythagorean_triplets(30),
                         [[3, 4, 5], [5, 12, 13], [6, 8, 10], [7, 24, 25],
                          [8, 15, 17], [9, 12, 15], [10, 24, 26], [12, 16, 20],
                          [15, 20, 25], [18, 24, 30], [20, 21, 29]])


if __name__ == "__main__":
    unittest.main()
