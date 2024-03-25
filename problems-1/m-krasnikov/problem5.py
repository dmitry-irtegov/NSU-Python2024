import unittest


def generate_sieve(number):
    prime = {i: True for i in range(number + 1)}
    primes = []
    p = 2
    while p ** 2 <= number:
        if prime[p]:
            primes.append(p)
            for i in range(p * p, number + 1, p):
                prime[i] = False
        p += 1

    return primes


def prime_factorization(number):
    primes = generate_sieve(number)
    cur_prime_index = 0
    factors = []

    while number > 1:
        if cur_prime_index == len(primes):
            factors.append([number, 1])
            return factors

        power = 0
        divisor = primes[cur_prime_index]
        while number % divisor == 0:
            number //= divisor
            power += 1
        if power > 0:
            factors.append([divisor, power])

        cur_prime_index += 1
    return factors


class TestPrimeFactorizationFunction(unittest.TestCase):
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

    def test_big_prime_number(self):
        self.assertEqual(prime_factorization(181081),
                         [[181081, 1]])


if __name__ == "__main__":
    unittest.main()
