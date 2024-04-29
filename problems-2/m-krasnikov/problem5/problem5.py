import unittest
from math import sqrt


def prime_numbers(n):
    if n < 2:
        raise ValueError("n must be greater than or equal to 2")
    return [number for number in range(2, n + 1)
            if all(number % div != 0
                   for div in range(2, int(sqrt(number)) + 1))
            ]


class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers(self):
        with self.assertRaises(ValueError):
            prime_numbers(1)
        self.assertEqual(prime_numbers(2), [2])
        self.assertEqual(prime_numbers(5), [2, 3, 5])
        self.assertEqual(prime_numbers(15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(prime_numbers(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


if __name__ == '__main__':
    unittest.main()
