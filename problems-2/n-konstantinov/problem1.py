from math import sqrt
from unittest import TestCase


def pythagorean_triples(n):
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c_squared = a ** 2 + b ** 2
            c = int(sqrt(c_squared))
            if c <= n and c_squared == c ** 2:
                yield a, b, c


def pythagorean_triples_list(n):
    return list(pythagorean_triples(n))


class TestPythagoreanTriples(TestCase):
    def test_pythagorean_triples_zero(self):
        self.assertEqual(pythagorean_triples_list(0), [])

    def test_pythagorean_triples_one(self):
        self.assertEqual(pythagorean_triples_list(1), [])

    def test_pythagorean_triples_five(self):
        self.assertEqual(pythagorean_triples_list(5), [(3, 4, 5)])

    def test_pythagorean_triples_ten(self):
        self.assertEqual(pythagorean_triples_list(10), [(3, 4, 5), (6, 8, 10)])

    def test_pythagorean_triples_twenty(self):
        expected_triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
        self.assertEqual(pythagorean_triples_list(20), expected_triples)

    def test_pythagorean_triples_fifty(self):
        expected_triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41),
                            (10, 24, 26), (11, 60, 61), (12, 16, 20), (12, 35, 37), (13, 84, 85), (14, 48, 50),
                            (15, 20, 25), (15, 36, 39), (16, 30, 34), (16, 63, 65), (18, 24, 30), (18, 80, 82),
                            (20, 21, 29), (20, 48, 52), (21, 28, 35), (21, 72, 75), (24, 32, 40), (24, 45, 51),
                            (24, 70, 74), (25, 60, 65), (27, 36, 45), (28, 45, 53), (28, 96, 100), (30, 40, 50),
                            (30, 72, 78), (32, 60, 68), (33, 44, 55), (33, 56, 65), (35, 84, 91), (36, 48, 60),
                            (36, 77, 85), (39, 52, 65), (39, 80, 89), (40, 42, 58), (40, 75, 85), (42, 56, 70),
                            (45, 60, 75), (48, 55, 73), (48, 64, 80), (51, 68, 85), (54, 72, 90), (57, 76, 95),
                            (60, 63, 87), (60, 80, 100), (65, 72, 97)]
        self.assertEqual(pythagorean_triples_list(100), expected_triples)

    def test_pythagorean_triples_check(self):
        triplets = pythagorean_triples(500)

        for triplet in triplets:
            a, b, c = triplet
            self.assertTrue(a ** 2 + b ** 2 == c ** 2)
