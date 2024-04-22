import math
import unittest


def factorize(x):
    multipliers = []
    upper_bound = math.ceil(math.sqrt(x + 1))
    i = 2
    while i <= upper_bound and x > 1:
        m = [i, 0]
        while x % i == 0:
            m[1] += 1
            x //= i
        if m[1] != 0:
            multipliers.append(m)
        i += 1

    if x > 1:
        multipliers.append([x, 1])

    return multipliers


class TestForFactorization(unittest.TestCase):
    def test_init_condition(self):
        self.assertEqual([[2, 2], [3, 1]], factorize(12))

    def test_init_condition_using_primes(self):
        self.assertEqual([[2, 2], [3, 1]], factorize(12))

    def test_prime_number(self):
        self.assertEqual([[236627, 1]], factorize(236627))

    def test_prime_number_using_primes(self):
        self.assertEqual([[236627, 1]], factorize(236627))

    def test_big_number(self):
        self.assertEqual([[2, 6], [5, 6], [31, 1]], factorize(31000000))

    def test_huge_number(self):
        self.assertEqual([[17, 2], [67, 1], [389, 1], [699059, 1]], factorize(5265457093213))


if __name__ == '__main__':
    unittest.main()
