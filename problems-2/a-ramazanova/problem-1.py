import unittest


def pythagorean_triplets(n):
    return [(x, y, z)
            for x in range(1, n + 1)
            for y in range(x, n + 1)
            for z in range(y, n + 1)
            if x ** 2 + y ** 2 == z ** 2]


class TestPythagoreanTriplets(unittest.TestCase):
    def test_pythagorean_triplets_1(self):
        self.assertEqual(pythagorean_triplets(1), [])

    def test_pythagorean_triplets_5(self):
        self.assertEqual(pythagorean_triplets(5), [(3, 4, 5)])

    def test_pythagorean_triplets_15(self):
        self.assertEqual(pythagorean_triplets(15), [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)])

    def test_pythagorean_triplets_500(self):
        actual_triplets = pythagorean_triplets(500)
        self.assertEqual(len(actual_triplets), 386)
        for triplet in actual_triplets:
            self.assertTrue(triplet[2] > triplet[1] >= triplet[0])
            self.assertEqual(triplet[0] ** 2 + triplet[1] ** 2, triplet[2] ** 2)
            self.assertTrue(triplet[2] <= 500)


if __name__ == '__main__':
    unittest.main()
