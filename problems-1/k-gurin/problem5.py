# problems-1/assignment-5
import unittest


def factorize(num):
    primes = []
    d = 2
    while num > 1 and d * d <= num:
        count = 0
        while num % d == 0:
            num //= d
            count += 1
        if count > 0:
            primes.append([d, count])
        d = d + 1
    if num > 1:
        primes.append([num, 1])
    return primes


class PrimeFactors(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorize(0), [])

    def test_one(self):
        self.assertEqual(factorize(1), [])

    def test_init(self):
        self.assertEqual(factorize(12), [[2, 2], [3, 1]])

    def test_prime(self):
        self.assertEqual(factorize(3571), [[3571, 1]])

    def test_power_of_two(self):
        self.assertEqual(factorize(16), [[2, 4]])

    def test_big(self):
        self.assertEqual(
            factorize(7420738134810),
            [
                [2, 1],
                [3, 1],
                [5, 1],
                [7, 1],
                [11, 1],
                [13, 1],
                [17, 1],
                [19, 1],
                [23, 1],
                [29, 1],
                [31, 1],
                [37, 1],
            ],
        )


if __name__ == '__main__':
    unittest.main()
