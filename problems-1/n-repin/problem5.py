import unittest
import io

from unittest.mock import patch

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


def print_formatted_primes_list(terms: list[tuple[int, int]]):
    if len(terms) == 0:
        return

    p, k = terms.pop(0)
    print(f"{p}^{k}", end='')

    for p, k in terms:
        print(f" * {p}^{k}", end='')

    print()

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

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_formatted_print_2(self, mock_stdout):
        print_formatted_primes_list(primes(2))
        self.assertEqual(mock_stdout.getvalue(), "2^1\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_formatted_print_big(self, mock_stdout):
        print_formatted_primes_list(primes(7468834))
        self.assertEqual(mock_stdout.getvalue(), "2^1 * 29^1 * 131^1 * 983^1\n")



if __name__ == "__main__":
    unittest.main()
