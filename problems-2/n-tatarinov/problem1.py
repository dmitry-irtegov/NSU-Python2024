from math import sqrt
import unittest


def get_triples(n):
    return [(x, y, int(sqrt(x ** 2 + y ** 2))) for x in range(1, n) for y in range(1, n) if
            sqrt(x ** 2 + y ** 2).is_integer() and sqrt(x ** 2 + y ** 2) <= n]


class TestTriples(unittest.TestCase):
    def test_1(self):
        triples = [(3, 4, 5), (4, 3, 5)]
        self.assertEquals(get_triples(6), triples)

    def test_2(self):
        triples = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
        self.assertEquals(get_triples(10), triples)

    def test_3(self):
        triples = [(3, 4, 5),
                   (4, 3, 5),
                   (5, 12, 13),
                   (6, 8, 10),
                   (8, 6, 10),
                   (8, 15, 17),
                   (9, 12, 15),
                   (12, 5, 13),
                   (12, 9, 15),
                   (12, 16, 20),
                   (15, 8, 17),
                   (16, 12, 20)]
        self.assertEquals(get_triples(20), triples)

if __name__ == '__main__':
    unittest.main()
