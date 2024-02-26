import unittest


def prime_factorization(number):
    primes = []
    divisor = 2
    while divisor * divisor <= number:
        count = 0
        while number % divisor == 0:
            number //= divisor
            count += 1
        if count > 0:
            primes.append([divisor, count])
        divisor += 1
    if number > 1:
        primes.append([number, 1])
    return primes


class TestFun(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(prime_factorization(0), [])

    def test_one(self):
        self.assertEqual(prime_factorization(1), [])

    def test_prime_number(self):
        self.assertEqual(prime_factorization(37), [[37, 1]])

    def test_number_12(self):
        self.assertEqual(prime_factorization(12),  [[2, 2], [3, 1]])

    def test_large_number(self):
        self.assertEqual(prime_factorization(1000000), [[2, 6], [5, 6]])


if __name__ == '__main__':
    unittest.main()
