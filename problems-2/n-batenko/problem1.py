import unittest
from math import sqrt

def pif_triple(n : int):
    if (n <= 0):
        raise Exception("Exception: In pif_triple input, n must be greater than zero.")
    
    result = []

    result = [(x, y, z) for x in range(1, int(sqrt(n)) + 1)
                for y in range(x, int(sqrt(n)) + 1)
                    for z in range(1, int(sqrt(n)) + 1)
                        if (z**2 == x**2 + y**2) and (z**2 <= n)]

    return result

class TestPifTriple(unittest.TestCase):

    def test_too_little_1(self):
        self.assertEqual(pif_triple(1), [])

    def test_too_little_5(self):
        self.assertEqual(pif_triple(5), [])

    def test_z10(self):
        self.assertEqual(pif_triple(100), [(3, 4, 5), (6, 8, 10)])
    
    def test_exception(self):
        with self.assertRaises(Exception) as context:
            pif_triple(-100)
        self.assertTrue("Exception: In pif_triple input, n must be greater than zero." in str(context.exception))

if __name__ == '__main__':
    unittest.main()