import unittest


def pythagorean_triples(n: int) -> list[tuple[int, int, int]]:
    return [ (a, b, c) for a in range(1, n) for b in range(1, n) for c in range(1, n) if a*a + b*b == c*c ]


class TestTriples(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(pythagorean_triples(5), [])

    def test_base(self):
        self.assertEqual(pythagorean_triples(6), [(3, 4, 5), (4, 3, 5)])

    def test_more_triples(self):
        self.assertEqual(pythagorean_triples(16), [(3, 4, 5), (4, 3, 5), (5, 12, 13), (6, 8, 10), (8, 6, 10), (9, 12, 15), (12, 5, 13), (12, 9, 15)])


if __name__ == "__main__":
    unittest.main()
