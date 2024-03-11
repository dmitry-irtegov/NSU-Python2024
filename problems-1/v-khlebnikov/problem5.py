import math
import time
import unittest


def get_primes(x):
    if not hasattr(get_primes, 'last_bound'):
        get_primes.last_bound = 0
    if not hasattr(get_primes, 'primes'):
        get_primes.primes = []

    if get_primes.last_bound < x:
        new_primes = list(range(x + 1))
        new_primes[1] = 0

        for i in range(2, math.ceil(math.sqrt(x))):
            if new_primes[i] != 0:
                j = 2 * i
                while j <= x:
                    new_primes[j] = 0
                    j = j + i

        if not get_primes.primes:
            get_primes.primes = [i for i in new_primes if i != 0]
        else:
            get_primes.primes = get_primes.primes + \
                                [i for i in new_primes[get_primes.last_bound:] if i != 0]

        get_primes.last_bound = x
    return get_primes.primes


def factorize(x, use_primes=True):
    multipliers = []
    for i in (get_primes(x) if use_primes else range(2, x + 1)):
        if x < i ** 2:
            if x != 1:
                multipliers.append([x, 1])
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
        self.assertEqual([[2, 2], [3, 1]], factorize(12, use_primes=False))

    def test_init_condition_using_primes(self):
        self.assertEqual([[2, 2], [3, 1]], factorize(12))

    def test_prime_number(self):
        self.assertEqual([[236627, 1]], factorize(236627, use_primes=False))

    def test_prime_number_using_primes(self):
        self.assertEqual([[236627, 1]], factorize(236627))

    # Из-за необходимости вычисления всех простых чисел до искомого числа,
    # использование метода с вычислением простых чисел приведёт к долгому вычислению результата
    def test_big_number(self):
        start = time.perf_counter()
        self.assertEqual([[2, 6], [5, 6], [31, 1]], factorize(31000000, use_primes=False))
        print("Without primes:", time.perf_counter() - start)

    def test_big_number_using_primes(self):
        start = time.perf_counter()
        self.assertEqual([[2, 6], [5, 6], [31, 1]], factorize(31000000))
        print("With primes (calculating primes):", time.perf_counter() - start)
        start = time.perf_counter()
        self.assertEqual([[2, 6], [5, 6], [31, 1]], factorize(31000000))
        print("With primes (using calculated primes):", time.perf_counter() - start)
        start = time.perf_counter()
        self.assertEqual([[2, 1], [3, 1], [11, 1], [83, 1], [5659, 1]], factorize(31000002))
        print("With primes (bigger number) (using calculated primes):", time.perf_counter() - start)

    def test_time_for_get_primes(self):
        start = time.perf_counter()
        get_primes(310000)
        res1 = time.perf_counter() - start
        start = time.perf_counter()
        get_primes(310000)
        res2 = time.perf_counter() - start
        self.assertLess(res2, res1)

    def test_primes_correctness(self):
        self.assertEqual(
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
             107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
             227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
             349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
             467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
             613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
             751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
             887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997],
            [num for num in get_primes(1000) if num <= 1000])


if __name__ == '__main__':
    unittest.main()
