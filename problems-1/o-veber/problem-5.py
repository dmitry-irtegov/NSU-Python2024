from math import ceil, sqrt
from unittest import TestCase, main


def get_primes_to_powers(digit):
    resulted_list = []
    for i in range(2, ceil(sqrt(digit)) + 1):
        if digit == 1:
            break
        result = 0
        while digit != 1 and digit % i == 0:
            digit /= i
            result += 1
        if result > 0:
            resulted_list.append((i, result))
    return resulted_list


assert get_primes_to_powers(12) == [(2, 2), (3, 1)]
assert get_primes_to_powers(0) == []
assert get_primes_to_powers(1) == []
assert get_primes_to_powers(2) == [(2, 1)]


class TestDictionary(TestCase):
    def test_zero(self):
        self.assertEqual([], get_primes_to_powers(0))

    def test_one(self):
        self.assertEqual([], get_primes_to_powers(1))

    def test_two(self):
        self.assertEqual([(2, 1)], get_primes_to_powers(2))

    def test_twelve(self):
        self.assertEqual([(2, 2), (3, 1)], get_primes_to_powers(12))

    def test_one_thousand(self):
        self.assertEqual([(2, 3), (5, 3)], get_primes_to_powers(1000))


if __name__ == "__main__":
    main()
