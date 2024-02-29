from math import sqrt
import unittest

def decompose_to_primes(n):

    def is_prime(num, primes):
        k = 1
        for i in range(2, int(sqrt(num)) + 1, k):
            if num in primes:
                return True
            else:
                if num % i == 0:
                    return False
            if i == 3:
                k += 1
        return True
    
    result = []
    primes = []

    num = abs(n)

    if num < 2:
        return [()]

    if not is_prime(num, primes):
        k = 1
        for factor in range(2, num // 2 + 1, k):
            if (not is_prime(factor, primes)):
                continue
            power = 0
            while num % factor == 0:
                num //= factor
                power += 1
            if (power == 0):
                continue
            else:
                primes.append(factor)
                result.append((factor, power))

            if factor == 3: k += 1
    else:
        result.append((num, 1))

    return result

class DecomposerTests(unittest.TestCase):
    def test_36(self):
        self.assertEqual(decompose_to_primes(36), [(2,2), (3,2)])
    
    def test_5(self):
        self.assertEqual(decompose_to_primes(5), [(5, 1)])
    
    def test_1(self):
        self.assertEqual(decompose_to_primes(1), [()])

if __name__ == '__main__':
    unittest.main()