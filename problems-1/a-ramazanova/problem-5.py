import unittest


def prime_factorization(n):
    result = []
    i = 2
    while i * i <= n:
        step = [i, 0]
        while n % i == 0:
            step[1] += 1
            n //= i
        if step[1] != 0:
            result.append(step)
        i += 1
    if n != 1:
        result.append([n, 1])
    return result


class TestPrimeFactorization(unittest.TestCase):
    def test_prime_factorization_2(self):
        self.assertEqual(prime_factorization(2), [[2, 1]])

    def test_prime_factorization_17(self):
        self.assertEqual(prime_factorization(17), [[17, 1]])

    def test_prime_factorization_31(self):
        self.assertEqual(prime_factorization(31), [[31, 1]])

    def test_prime_factorization_12(self):
        self.assertEqual(prime_factorization(12), [[2, 2], [3, 1]])

    def test_prime_factorization_90(self):
        self.assertEqual(prime_factorization(90), [[2, 1], [3, 2], [5, 1]])

    def test_prime_factorization_100(self):
        self.assertEqual(prime_factorization(100), [[2, 2], [5, 2]])

    def test_prime_factorization_31010762653(self):
        self.assertEqual(prime_factorization(31010762653), [[13, 5], [17, 4]])

    def test_prime_factorization_2176782336000(self):
        self.assertEqual(prime_factorization(2176782336000), [[2, 15], [3, 12], [5, 3]])

    def test_prime_factorization_1628413597910449(self):
        self.assertEqual(prime_factorization(1628413597910449), [[7, 18]])

    def test_prime_factorization_284050286302389(self):
        self.assertEqual(prime_factorization(284050286302389), [[3, 1], [2777, 2], [3491, 1], [3517, 1]])

    def test_prime_factorization_19631060871031905047766960690917(self):
        self.assertEqual(prime_factorization(19631060871031905047766960690917), [[2963, 1], [2969, 1], [2971, 1],
                                                                                 [2999, 1], [3001, 1], [3011, 1],
                                                                                 [3019, 1], [3023, 1], [3037, 1]])

    def test_prime_factorization_20999999(self):
        self.assertEqual(prime_factorization(20999999), [[20999999, 1]])


if __name__ == '__main__':
    unittest.main()
