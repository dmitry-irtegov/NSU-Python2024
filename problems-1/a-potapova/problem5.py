import unittest


def into_prime_numbers(number: int) -> list:
    result = []
    current_number = number
    divisor = 2
    power = 0
    while current_number != 1:
        while current_number % divisor == 0:
            current_number = current_number // divisor
            power += 1
        if power > 0:
            result.append([divisor, power])
            power = 0
        divisor += 1
    return result


class TestIntoPrimeNumbers(unittest.TestCase):
    def test_into_prime_numbers(self):
        self.assertEqual(into_prime_numbers(6), [[2, 1], [3, 1]])
        self.assertEqual(into_prime_numbers(9), [[3, 2]])
        self.assertEqual(into_prime_numbers(21), [[3, 1], [7, 1]])


if __name__ == '__main__':
    unittest.main()
