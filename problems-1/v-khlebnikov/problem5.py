import math
import time
import unittest

primes = {"last_bound": 0, "primes": []}


def get_primes(x):
    if primes["last_bound"] < x:
        primes["last_bound"] = x
        new_primes = [i for i in range(x + 1)]
        new_primes[1] = 0
        for i in range(2, math.floor(math.sqrt(x + 1))):
            if new_primes[i] != 0:
                j = 2 * i
                while j <= x:
                    new_primes[j] = 0
                    j = j + i
        primes["primes"] = [i for i in new_primes if i != 0]
    return primes["primes"]


def factorize(x, use_primes=True):
    multipliers = []
    for i in (get_primes(x) if use_primes else range(2, x + 1)):
        if x == 1:
            break
        m = [i, 0]
        while x % i == 0:
            m[1] += 1
            x /= i
        if m[1] != 0:
            multipliers.append(m)
    return multipliers


class TestForFactorization(unittest.TestCase):
    def test_init_condition(self):
        self.assertEqual(factorize(12, use_primes=False), [[2, 2], [3, 1]])

    def test_init_condition_using_primes(self):
        self.assertEqual(factorize(12), [[2, 2], [3, 1]])

    def test_prime_number(self):
        self.assertEqual(factorize(236627, use_primes=False), [[236627, 1]])

    def test_prime_number_using_primes(self):
        self.assertEqual(factorize(236627), [[236627, 1]])

    # Из-за необходимости вычисления всех простых чисел до искомого числа,
    # использование метода с простыми числами приведёт к долгому вычислению результата
    def test_big_number(self):
        start = time.perf_counter()
        self.assertEqual(factorize(31000000, use_primes=False), [[2, 6], [5, 6], [31, 1]])
        print("Without primes:", time.perf_counter() - start)

    def test_big_number_using_primes(self):
        start = time.perf_counter()
        self.assertEqual(factorize(31000000), [[2, 6], [5, 6], [31, 1]])
        print("With primes (calculating primes):", time.perf_counter() - start)
        start = time.perf_counter()
        self.assertEqual(factorize(31000000), [[2, 6], [5, 6], [31, 1]])
        print("With primes (using calculated primes):", time.perf_counter() - start)


if __name__ == '__main__':
    unittest.main()
