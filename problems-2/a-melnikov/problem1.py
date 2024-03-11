import unittest


def generate_pythagorian_triples(n: int) -> {(int, int, int)}:
    triples = set()
    for x in range(3, n + 1):
        for y in range(x, n + 1):
            for z in range(y, n + 1):
                if x * x + y * y == z * z:
                    triples.add((x, y, z))

    return triples


class TestPythagorianTriples(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(generate_pythagorian_triples(-15), set())

    def test_zero(self):
        self.assertEqual(generate_pythagorian_triples(0), set())

    def test_one(self):
        self.assertEqual(generate_pythagorian_triples(2), set())

    def test_big(self):
        self.assertEqual(
            generate_pythagorian_triples(30),
            {
                (3, 4, 5),
                (6, 8, 10),
                (5, 12, 13),
                (9, 12, 15),
                (8, 15, 17),
                (12, 16, 20),
                (7, 24, 25),
                (10, 24, 26),
                (20, 21, 29),
                (18, 24, 30),
                (15, 20, 25),
            },
        )


if __name__ == "__main__":
    unittest.main()
