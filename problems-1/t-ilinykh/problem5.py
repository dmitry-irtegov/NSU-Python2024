import unittest

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor
        if count > 0:
            factors.append([divisor, count])
        divisor += 1

    return factors

class TestPrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        number = 12
        expected_factors = [[2, 2], [3, 1]]
        self.assertEqual(prime_factors(number), expected_factors)

    def test_large_number(self):
        number = 84
        expected_factors = [[2, 2], [3, 1], [7, 1]]
        self.assertEqual(prime_factors(number), expected_factors)

    def test_prime_number(self):
        number = 17
        expected_factors = [[17, 1]]
        self.assertEqual(prime_factors(number), expected_factors)

    def test_zero(self):
        number = 0
        expected_factors = []
        self.assertEqual(prime_factors(number), expected_factors)

    def test_negative_number(self):
        number = -10
        expected_factors = []
        self.assertEqual(prime_factors(number), expected_factors)

if __name__ == '__main__':
    unittest.main()

