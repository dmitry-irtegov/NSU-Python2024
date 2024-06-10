import unittest


def factorize_number(num):
    if num == 1:
        return [[1, 1]]
    elif num < 1:
        raise ValueError("Number must be positive")

    factor = 2
    factor_list = []

    while factor * factor <= num:
        power_list = [factor, 0]
        while num % factor == 0:
            power_list[1] += 1
            num //= factor
        if power_list[1] > 0:
            factor_list.append(power_list)
        factor += 1

    if num > 1:
        factor_list.append([num, 1])

    return factor_list


class TestFactorizeNumber(unittest.TestCase):

    def test_factorize_simple_number(self):
        self.assertEqual([[2, 1], [3, 2], [7, 1]], factorize_number(126))

    def test_factorize_prime_degree(self):
        self.assertEqual([[5, 4]], factorize_number(625))

    def test_factorize_one(self):
        self.assertEqual([[1, 1]], factorize_number(1))

    def test_factorize_prime_number(self):
        self.assertEqual([[13, 1]], factorize_number(13))

    def test_factorize_large_number(self):
        self.assertEqual([[2, 1], [3, 1], [17, 1], [43, 1]], factorize_number(2 * 3 * 17 * 43))

    def test_factorize_power_of_two(self):
        self.assertEqual([[2, 10]], factorize_number(1024))

    def test_factorize_mixed_factors(self):
        self.assertEqual([[2, 3], [5, 2], [11, 1]], factorize_number(2200))

    def test_factorize_repeated_primes(self):
        self.assertEqual([[2, 3], [3, 2]], factorize_number(72))

    def test_factorize_large_prime(self):
        self.assertEqual([[104729, 1]], factorize_number(104729))  # 104729 is a large prime number

    def test_factorize_large_composite(self):
        self.assertEqual([[2, 1], [3, 3], [7, 2], [19, 1], [97, 1]], factorize_number(2 * 3**3 * 7**2 * 19 * 97))

    def test_factorize_product_of_large_primes(self):
        self.assertEqual([[10007, 1], [10009, 1], [10037, 1]], factorize_number(10007 * 10009 * 10037))


if __name__ == "__main__":
    unittest.main()
