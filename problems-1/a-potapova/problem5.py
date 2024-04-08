import math
import unittest


def into_prime_numbers(number: int) -> list:
    result = []
    current_number = number
    power = 0
    for divisor in range(2, int(math.sqrt(number)) + 1):
        while current_number % divisor == 0:
            current_number = current_number // divisor
            power += 1
        if power > 0:
            result.append([divisor, power])
            power = 0
        if current_number == 1:
            return result
    if current_number != 1:
        result.append([current_number, 1])
    return result


class TestIntoPrimeNumbers(unittest.TestCase):
    def test_into_prime_numbers(self):
        self.assertEqual(into_prime_numbers(6), [[2, 1], [3, 1]])
        self.assertEqual(into_prime_numbers(9), [[3, 2]])
        self.assertEqual(into_prime_numbers(21), [[3, 1], [7, 1]])
        self.assertEqual(into_prime_numbers(31), [[31, 1]])
        big_prime_number = int(math.pow(2, 31) - 1)
        self.assertEqual(into_prime_numbers(big_prime_number), [[big_prime_number, 1]])


if __name__ == '__main__':
    unittest.main()
