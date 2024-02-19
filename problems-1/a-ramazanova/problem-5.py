import unittest

primes = []


def is_prime(a):
    if a in primes:
        return True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0 and a != i:
            return False
    primes.append(a)
    return True


def prime_factorization(number):
    result = []
    i = 1
    if is_prime(number):
        return [[number, 1]]
    while number != 1:
        i += 1
        if is_prime(i) and number % i == 0:
            step = [i, 0]
            while number % i == 0:
                step[1] += 1
                number /= i
            result.append(step)
    return result


class TestIsPrime(unittest.TestCase):
    def test_is_prime_with_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(31))

    def test_is_prime_with_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(25))


class TestPrimeFactorization(unittest.TestCase):
    def test_prime_factorization_with_primes(self):
        self.assertEqual(prime_factorization(2), [[2, 1]])
        self.assertEqual(prime_factorization(17), [[17, 1]])
        self.assertEqual(prime_factorization(31), [[31, 1]])

    def test_prime_factorization_with_composites(self):
        self.assertEqual(prime_factorization(12), [[2, 2], [3, 1]])
        self.assertEqual(prime_factorization(90), [[2, 1], [3, 2], [5, 1]])
        self.assertEqual(prime_factorization(100), [[2, 2], [5, 2]])
        self.assertEqual(prime_factorization(31010762653), [[13, 5], [17, 4]])
        self.assertEqual(prime_factorization(2176782336000), [[2, 15], [3, 12], [5, 3]])
        self.assertEqual(prime_factorization(1628413597910449), [[7, 18]])


if __name__ == '__main__':
    unittest.main()
