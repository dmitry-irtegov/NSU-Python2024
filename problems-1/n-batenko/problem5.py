from math import sqrt
import unittest

def decompose_to_primes(n):    
    num = abs(n)

    if num < 2:
        return [()]
    
    result = []
    primes = []
    
    def is_prime(num):
        if num in primes:
            return True
        
        k = 1
        for i in range(2, int(sqrt(num)) + 1, k):
            if num % i == 0:
                return False

            if i == 3:
                k += 1
        
        if (num not in primes):
            primes.append(num)

        return True

    if is_prime(num):
        return [(num, 1)]
    
    k = 1
    for factor in range(2, num // 2 + 1, k):
        if (not is_prime(factor)):
            continue

        power = 0
        while num % factor == 0:
            num //= factor
            power += 1
                
        if (power == 0):
            continue
        else:
            result.append((factor, power))

        if factor == 3: 
            k = k + 1

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
