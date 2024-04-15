import unittest

def pif_triple(n : int):
    if (n <= 0):
        raise Exception("Exception: In pif_triple input, n must be greater than zero.")
    
    return [(x, y, z)
            for x in range(1, n + 1)
            for y in range(x, n + 1)
            for z in range(y, n + 1)
            if (x**2 + y**2 == z**2)]


class TestPifTriple(unittest.TestCase):

    def test_too_little_1(self):
        self.assertEqual(pif_triple(1), [])

    def test_too_5(self):
        self.assertEqual(pif_triple(5), [(3, 4, 5)])

    def test_z10(self):
        self.assertEqual(pif_triple(10), [(3, 4, 5), (6, 8, 10)])
    
    def test_exception(self):
        with self.assertRaises(Exception) as context:
            pif_triple(-100)
        self.assertTrue("Exception: In pif_triple input, n must be greater than zero." in str(context.exception))

if __name__ == '__main__':
    unittest.main()

print(pif_triple(10))
