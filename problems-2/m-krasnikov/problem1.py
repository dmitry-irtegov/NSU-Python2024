import unittest


def generate_pythagorean_triplets(number):
    return [
        [x, y, z]
        for x in range(1, number + 1)
        for y in range(x, number + 1)
        for z in range(y, number + 1)
        if x ** 2 + y ** 2 == z ** 2
    ]


class TestPythagoreanTripletsGenerator(unittest.TestCase):

    def test(self):
        self.assertEqual(generate_pythagorean_triplets(30),
                         [[3, 4, 5], [5, 12, 13], [6, 8, 10], [7, 24, 25],
                          [8, 15, 17], [9, 12, 15], [10, 24, 26], [12, 16, 20],
                          [15, 20, 25], [18, 24, 30], [20, 21, 29]])


if __name__ == "__main__":
    unittest.main()
