import unittest
import math

def gen_pytha_triples(n):
    triples = []
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            z_square = math.pow(x, 2) + math.pow(y, 2)
            z = int(math.sqrt(z_square))
            if z <= n and math.pow(z, 2) == z_square:
                triples.append((x, y, z))
    return triples

class TestPythagoreanTriples(unittest.TestCase):
    def test_gen_pytha_triples(self):
        test_cases = [5, 10, 15, 20, 25, 30, 35]
        for n in test_cases:
            triples = gen_pytha_triples(n)
            for triple in triples:
                x, y, z = triple
                self.assertTrue(math.pow(x, 2) + math.pow(y, 2) == math.pow(z, 2),
                                f"Triple {triple} is not a Pythagorean triple.")

    def test_empty_case(self):
        # Testing with n = 1, where no Pythagorean triple exists
        n = 1
        triples = gen_pytha_triples(n)
        self.assertEqual(triples, [], "No Pythagorean triple should exist for n = 1")

    def test_large_n(self):
        # Testing with a large value of n
        n = 100
        triples = gen_pytha_triples(n)
        for triple in triples:
            x, y, z = triple
            self.assertTrue(math.pow(x, 2) + math.pow(y, 2) == math.pow(z, 2),
                            f"Triple {triple} is not a Pythagorean triple.")

if __name__ == '__main__':
    unittest.main()
