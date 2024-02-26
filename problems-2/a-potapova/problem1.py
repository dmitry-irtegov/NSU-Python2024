import unittest


def pythagorean_triplets(n: int):
    return [(x, y, z)
            for x in range(1, n + 1)
            for y in range(x, n + 1)
            for z in range(y, n + 1)
            if x ** 2 + y ** 2 == z ** 2]


class TestPythagoreanTriplets(unittest.TestCase):
    def test_pythagorean_triplets(self):
        self.assertEqual(pythagorean_triplets(1), [])
        self.assertEqual(pythagorean_triplets(5), [(3, 4, 5)])
        self.assertEqual(pythagorean_triplets(15), [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)])


if __name__ == '__main__':
    unittest.main()
