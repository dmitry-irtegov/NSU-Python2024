import unittest
import math
import random


def gen_pytha_triples(n):
    triples = []
    for x in range (1, n+1):
        for y in range(x, n+1):
            for z in range(y, n+1):
                if math.sqrt(x) + math.sqrt(y) == math.sqrt(z):
                    triples.append((x,y,z))
    return triples

class TestPythagoreanTriples(unittest.TestCase):
    def test_gen_pytha_triples(self):
        for i in range(15):
            n = random.randint(1, 200)
            expected_triples = gen_pytha_triples(n)
            self.assertEqual(gen_pytha_triples(n), expected_triples)

if __name__ == '__main__':
    unittest.main()

