from math import sqrt
import unittest

def decompose_to_primes(n : int):    
    num = abs(n)

    if num < 2:
        return (())
    
    result = []
    
    power = 0
    while num % 2 == 0:
        num //= 2
        power += 1
                
    if (power != 0):
        result.append((2, power)) 

    for factor in range(3, int(sqrt(num)) + 3, 2):
        if (1 < num <= factor):
            result.append((num, 1))
            break

        power = 0
        while num % factor == 0:
            num //= factor
            power += 1
                
        if (power == 0):
            continue
        else:
            result.append((factor, power))

    if abs(n) > 1 and result == []:
        return ((abs(n), 1))

    return tuple(map(lambda t: (t[0], t[1]), result))

class DecomposerTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(decompose_to_primes(1), (()))

    def test_5(self):
        self.assertEqual(decompose_to_primes(5), ((5, 1)))
    
    def test_6(self):
        self.assertEqual(decompose_to_primes(6), ((2, 1), (3, 1)))

    def test_36(self):
        self.assertEqual(decompose_to_primes(36), ((2, 2), (3, 2)))
    
    def test_1000(self):
        self.assertEqual(decompose_to_primes(1000), ((2, 3), (5, 3)))

    def test_1234554321(self):
        self.assertEqual(decompose_to_primes(1234554321), ((3, 1), (7, 1), (11, 1), (13, 1), (37, 1), (41, 1), (271, 1)))

if __name__ == '__main__':
    unittest.main()
