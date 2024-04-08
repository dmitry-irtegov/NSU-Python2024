import unittest

from typing_extensions import List


def solve(n: int) -> List[int]:
    return [number for number in range(2, n + 1)
            if (number % 2
                and all([number % divisor
                         for divisor in range(3, int(number ** 0.5) + 1, 2)])
                or number == 2)]


class TestPrimes(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solve(1), [])
        self.assertEqual(solve(10), [2, 3, 5, 7])
        self.assertEqual(solve(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                      41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


if __name__ == '__main__':
    unittest.main()
