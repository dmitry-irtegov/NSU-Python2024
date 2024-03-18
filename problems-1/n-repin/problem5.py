import unittest

from math import ceil, sqrt


def primes(number: int) -> list[tuple[int, int]]:
    prime_list = []
    divisor = 2
    
    while divisor <= ceil(sqrt(number)):
        power = 0
        
        while number % divisor == 0:
            power += 1
            number //= divisor

        if power > 0:
            prime_list.append((divisor, power))

        divisor += 1

    if number > 1:
        prime_list.append((number, 1))

    return prime_list


def format_primes_list(map: list[tuple[int, int]]) -> str:
    terms = []

    for item in map:
        (p, k) = item
        terms.append(f"{p}^{k}")

    return " * ".join(terms)


class TestPrimes(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(primes(2), [(2, 1)])

    def test_prime(self):
        self.assertEqual(primes(31), [(31, 1)])

    def test_non_trivial(self):
        self.assertEqual(primes(30), [(2, 1), (3, 1), (5, 1)])

    def test_powers(self):
        self.assertEqual(primes(1280), [(2, 8), (5, 1)])

    def test_big(self):
        self.assertEqual(primes(7468834), [(2, 1), (29, 1), (131, 1), (983, 1)])

if __name__ == "__main__":
    unittest.main()
