# problems-1/assignment-5
import math
import unittest


def factorize(num):
    primes = []
    for d in range(2, int(math.sqrt(num)) + 1):
        count = 0
        while num % d == 0:
            num //= d
            count += 1
        if count > 0:
            primes.append([d, count])
    if num > 1:
        primes.append([num, 1])
    return primes


class PrimeFactors(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorize(0), [])

    def test_one(self):
        self.assertEqual(factorize(1), [])

    def test_init(self):
        self.assertEqual(factorize(12), [[2, 2], [3, 1]])

    def test_prime(self):
        self.assertEqual(factorize(3571), [[3571, 1]])

    def test_big_split_number(self):
        self.assertEqual(factorize(124542), [[2, 1], [3, 2], [11, 1], [17, 1], [37, 1]])


if __name__ == '__main__':
    unittest.main()
