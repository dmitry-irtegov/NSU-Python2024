
import unittest

def factorize_number(n):
    if n <= 1:
        return []

    max_divisor = int(abs(n) ** 0.5) + 1
    counts = [0] * (max_divisor + 1)

    divisor = 2
    while n > 1 and divisor <= max_divisor:
        while n % divisor == 0:
            counts[divisor] += 1
            n //= divisor
        divisor += 1

    factors = [[i, counts[i]] for i in range(len(counts)) if counts[i] > 0]

    factors_size = len(factors) + (n > 1)
    factors_result = [[0, 0]] * factors_size

    for i, factor in enumerate(factors):
        factors_result[i] = factor

    if n > 1:
        factors_result[len(factors)] = [n, 1]

    return factors_result

class TestFactorizeNumber(unittest.TestCase):
    def test_prime_factors(self):
        number = 12
        expected_factors = [[2, 2], [3, 1]]
        self.assertEqual(factorize_number(number), expected_factors)

    def test_large_number(self):
        number = 84
        expected_factors = [[2, 2], [3, 1], [7, 1]]
        self.assertEqual(factorize_number(number), expected_factors)

    def test_prime_number(self):
        number = 17
        expected_factors = [[17, 1]]
        self.assertEqual(factorize_number(number), expected_factors)

    def test_zero(self):
        number = 0
        expected_factors = []
        self.assertEqual(factorize_number(number), expected_factors)

    def test_negative_number(self):
        number = -10
        expected_factors = []
        self.assertEqual(factorize_number(number), expected_factors)

if __name__ == '__main__':
    unittest.main()