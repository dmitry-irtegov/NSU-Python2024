import unittest


def factorize_number(num):
    if num == 1:
        return [1, 1]
    elif num < 1:
        raise ValueError("Number must be positive")

    prime = 2
    factor_list = []

    while prime * prime <= num:
        power_list = [prime, 0]
        while num % prime == 0:
            power_list[1] += 1
            num //= prime
        if power_list[1] > 0:
            factor_list.append(power_list)
        prime += 1

    if num > 1:
        factor_list.append([num, 1])

    return factor_list


class TestFactorizeNumber(unittest.TestCase):

    def test_factorize_simple_number(self):
        self.assertEquals([[2, 1], [3, 2], [7, 1]], factorize_number(126))

    def test_factorize_prime_degree(self):
        self.assertEquals([[5, 4]], factorize_number(625))

    def test_factorize_negative(self):
        self.assertRaises(ValueError, factorize_number, -1)

    def test_factorize_zero(self):
        self.assertRaises(ValueError, factorize_number, 0)


if __name__ == "__main__":
    unittest.main()