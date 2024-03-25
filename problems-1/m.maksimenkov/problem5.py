import math
import unittest


def prime_divisors(num):
    result = []
    if num == 0:
        return result
    elif num < 0:
        num = abs(num)
    for divisor in range(2, round(math.sqrt(num)) + 1):
        degree = 0
        if num % divisor == 0:
            while num % divisor == 0:
                num //= divisor
                degree += 1
            result.append([divisor, degree])
    if num != 1:
        result.append([num, 1])
    return result


class PrimeDivisorsTest(unittest.TestCase):

    def test(self):
        self.assertEqual(prime_divisors(0), [])
        self.assertEqual(prime_divisors(1), [])
        self.assertEqual(prime_divisors(-123), [[3, 1], [41, 1]])
        self.assertEqual(prime_divisors(123), [[3, 1], [41, 1]])
        self.assertEqual(prime_divisors(562), [[2, 1], [281, 1]])
        self.assertEqual(prime_divisors(12), [[2, 2], [3, 1]])

    def test_performance(self):
        print(prime_divisors(453526297733342))


if '__main__' == __name__:
    unittest.main()
