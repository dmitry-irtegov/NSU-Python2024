import unittest


def pythagorean_triples(n):
    return [(a, b, c)
            for a in range(1, n + 1)
            for b in range(a, n + 1)
            for c in range(b, n + 1)
            if a * a + b * b == c * c]


class TestPythagoreanTriples(unittest.TestCase):
    def test_pythagorean_triples(self):
        self.assertEqual(pythagorean_triples(5), [(3, 4, 5)])
        self.assertEqual(pythagorean_triples(10), [(3, 4, 5), (6, 8, 10)])
        self.assertEqual(pythagorean_triples(20),
                         [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)])
        self.assertEqual(pythagorean_triples(30),
                         [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26),
                          (12, 16, 20), (15, 20, 25), (18, 24, 30), (20, 21, 29)])
        self.assertEqual(pythagorean_triples(50),
                         [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41),
                          (10, 24, 26), (12, 16, 20), (12, 35, 37), (14, 48, 50), (15, 20, 25), (15, 36, 39),
                          (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45), (30, 40, 50)])


if __name__ == '__main__':
    unittest.main()
