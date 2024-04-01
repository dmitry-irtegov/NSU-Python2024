import unittest
from math import sqrt, modf


def generate_pythagorean_triplets(number):
    return [
        [x, y, int(z)]
        for x in range(1, number + 1)
        for y in range(x, number + 1)
        for z in [sqrt(x ** 2 + y ** 2)]
        if z <= number and modf(z)[0] == 0
    ]


class TestPythagoreanTripletsGenerator(unittest.TestCase):

    def test(self):
        self.assertEqual(generate_pythagorean_triplets(30),
                         [[3, 4, 5], [5, 12, 13], [6, 8, 10], [7, 24, 25],
                          [8, 15, 17], [9, 12, 15], [10, 24, 26], [12, 16, 20],
                          [15, 20, 25], [18, 24, 30], [20, 21, 29]])

    def test_large_number(self):
        triplets = generate_pythagorean_triplets(100)

        self.assertEqual(len(triplets), 52)
        for triplet in triplets:
            self.assertEqual(triplet[0] ** 2 + triplet[1] ** 2, triplet[2] ** 2)


if __name__ == "__main__":
    unittest.main()
