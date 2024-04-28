import unittest
from math import sqrt

def pif_triple(n : int):
    if (n <= 0):
        raise Exception("Exception: In pif_triple input, n must be greater than zero.")
    
    return [(x, y, int(sqrt(x**2 + y**2)))
            for x in range(1, n)
            for y in range(1, n)
            if sqrt(x**2 + y**2).is_integer() and x**2 + y**2 <= n**2]


class TestPifTriple(unittest.TestCase):

    def test_too_little_1(self):
        self.assertEqual(pif_triple(1), [])

    def test_too_5(self):
        self.assertEqual(pif_triple(5), [(3, 4, 5), (4, 3, 5)])

    def test_z10(self):
        self.assertEqual(pif_triple(10), [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)])
    
    def test_any(self, num = 1000):
        for (x, y, z) in pif_triple(num):
            self.assertTrue(x**2 + y**2 == z**2 & z**2 <= num ** 2)

    def test_exception(self):
        with self.assertRaises(Exception) as context:
            pif_triple(-100)
        self.assertTrue("Exception: In pif_triple input, n must be greater than zero." in str(context.exception))

if __name__ == '__main__':
    unittest.main()