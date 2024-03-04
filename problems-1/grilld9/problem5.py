import math
import unittest


def prime_divisors(num):
    result = []
    if num == 0:
        return result
    elif num < 0:
        num = abs(num)
    elif num == 1:
        return [1]
    idx = 0
    divisor = 2
    while num != 1:
        if is_simple(divisor):
            if num % divisor == 0:
                degree = 1
                result.append([divisor, degree])
                num //= divisor
                while num % divisor == 0:
                    degree += 1
                    result[idx][1] = degree
                    num //= divisor
                idx += 1
        divisor += 1
    return result
def is_simple(num):
    sqrt_rounded = round(math.sqrt(num))
    for i in range(2, sqrt_rounded + 1):
        if num % i == 0:
            return False
    return True
class PrimeDivisorsTest(unittest.TestCase):

    def test(self):
        self.assertEqual(prime_divisors(0), [])
        self.assertEqual(prime_divisors(1), [1])
        self.assertEqual(prime_divisors(-123), [[3, 1], [41, 1]])
        self.assertEqual(prime_divisors(123), [[3, 1], [41, 1]])
        self.assertEqual(prime_divisors(562), [[2, 1], [281, 1]])
        self.assertEqual(prime_divisors(12), [[2, 2], [3, 1]])
