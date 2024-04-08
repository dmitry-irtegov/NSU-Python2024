import unittest


def factorize_number(num: int) -> list[list[int]]:
    factors: list[list[int]] = []
    i: int = 2
    n: int = num
    while n > 1 and i * i <= num:
        count: int = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append([i, count])

        i += 1

    if n > 1:
        factors.append([num, 1])

    return factors


class TestFactorNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorize_number(0), [])

    def test_one(self):
        self.assertEqual(factorize_number(1), [])

    def test_two(self):
        self.assertEqual(factorize_number(2), [[2, 1]])

    def test_twelve(self):
        self.assertEqual(factorize_number(12), [[2, 2], [3, 1]])

    def test_big(self):
        self.assertEqual(
            factorize_number(7420738134810),
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

    def test_big_prime(self):
        self.assertEqual(factorize_number(789456126163), [[789456126163, 1]])


if __name__ == "__main__":
    unittest.main()
