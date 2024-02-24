import unittest


def prime_factorization(number):
    factors = []
    divisor = 2

    while number > 1:
        power = 0
        while number % divisor == 0:
            number //= divisor
            power += 1
        if power > 0:
            factors.append([divisor, power])
        divisor += 1
    return factors


class TestTrimSequenceFunction(unittest.TestCase):
    def test_one(self):
        self.assertEqual(prime_factorization(1), [])

    def test_prime_number(self):
        self.assertEqual(prime_factorization(23), [[23, 1]])

    def test_small_number(self):
        self.assertEqual(prime_factorization(18),
                         [[2, 1], [3, 2]])

    def test_big_number(self):
        self.assertEqual(prime_factorization(43560),
                         [[2, 3], [3, 2], [5, 1], [11, 2]])


if __name__ == "__main__":
    unittest.main()
