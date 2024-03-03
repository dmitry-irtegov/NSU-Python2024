import unittest


def pythagorean_triples(limits):
    if limits <= 0:
        raise ValueError("Limit cannot be less or equal zero.")

    return [(a, b, c) for m in range(2, limits) for n in range(1, m)
            for a, b, c in [(m * m - n * n, 2 * m * n, m * m + n * n)]
            if c <= limits]


class TestPythagoreanTriples(unittest.TestCase):

    def test_small_number(self):
        answer = [(3, 4, 5), (8, 6, 10), (5, 12, 13), (15, 8, 17), (12, 16, 20)]
        self.assertEquals(answer, pythagorean_triples(20))

    def test_big_number(self):
        answer = [(3, 4, 5), (8, 6, 10), (5, 12, 13), (15, 8, 17),
                  (12, 16, 20), (7, 24, 25), (24, 10, 26), (21, 20, 29),
                  (16, 30, 34), (9, 40, 41), (35, 12, 37), (32, 24, 40),
                  (27, 36, 45), (20, 48, 52), (11, 60, 61), (48, 14, 50),
                  (45, 28, 53), (40, 42, 58), (33, 56, 65), (24, 70, 74), (13, 84, 85),
                  (63, 16, 65), (60, 32, 68), (55, 48, 73), (48, 64, 80), (39, 80, 89),
                  (28, 96, 100), (80, 18, 82), (77, 36, 85), (72, 54, 90), (65, 72, 97)]
        self.assertEquals(answer, pythagorean_triples(100))

    def test_zero(self):
        self.assertRaises(ValueError, pythagorean_triples, 0)

    def test_negative_number(self):
        self.assertRaises(ValueError, pythagorean_triples, -1)


if __name__ == "__main__":
    unittest.main()
