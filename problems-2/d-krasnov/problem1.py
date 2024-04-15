import unittest


def pythagorean_triplet(n):
    """
    Function to find pythagorean triplets up to a given number.
    """
    return [(x, y, z) for x in range(1, n + 1) for y in range(x, n + 1) for z in range(y, n + 1) if
            x ** 2 + y ** 2 == z ** 2]


class TestPythagoreanTriples(unittest.TestCase):
    def test_pythagorean_triples(self):
        self.assertEqual([(3, 4, 5)], pythagorean_triplet(5))
        self.assertEqual([(3, 4, 5), (6, 8, 10)], pythagorean_triplet(10))
        self.assertEqual([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)],
                         pythagorean_triplet(20))
        self.assertEqual([], pythagorean_triplet(1))
        self.assertEqual([], pythagorean_triplet(0))
        self.assertEqual([], pythagorean_triplet(-2))

    def test_large_n(self):
        triplets = pythagorean_triplet(600)

        for triplet in triplets:
            x, y, z = triplet
            self.assertTrue(x ** 2 + y ** 2 == z ** 2, f"Triple {triplet} is not a Pythagorean triple.")
