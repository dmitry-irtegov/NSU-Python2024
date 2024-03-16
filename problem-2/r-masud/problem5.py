import unittest
import math

def generate_primes(limit):
    if limit < 2:
        return []

    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [i for i in range(limit + 1) if primes[i]]




class TestGeneratePrimes(unittest.TestCase):
    def test_generate_primes(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])
        self.assertEqual(generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(generate_primes(1), [])
        self.assertEqual(generate_primes(2), [2])
        self.assertEqual(generate_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

if __name__ == "__main__":
    unittest.main()
