import unittest


def prime_numbers(n: int):
    if n < 2:
        raise ValueError("n must be greater than or equal to 2")
    return [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]


class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers(self):
        with self.assertRaises(ValueError):
            prime_numbers(1)
        self.assertEqual(prime_numbers(2), [2])
        self.assertEqual(prime_numbers(5), [2, 3, 5])
        self.assertEqual(prime_numbers(15), [2, 3, 5, 7, 11, 13])


if __name__ == '__main__':
    unittest.main()
