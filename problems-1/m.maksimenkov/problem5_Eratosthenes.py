import math
import unittest


def sieve_of_eratosthenes(num):
    result = []
    if num == 0:
        return result
    elif num < 0:
        num = abs(num)
    sqrt_num = round(math.sqrt(num)) + 1
    sieve = [0] * sqrt_num
    for divisor in range(2, sqrt_num):
        if sieve[divisor] == 0:
            if num % divisor == 0:
                degree = 0
                while num % divisor == 0:
                    num //= divisor
                    degree += 1
                result.append([divisor, degree])
            for i in range(divisor, sqrt_num, divisor):
                sieve[i] = 1
    if num != 1:
        result.append([num, 1])
    return result


class PrimeDivisorsTest(unittest.TestCase):

    def test(self):
        self.assertEqual(sieve_of_eratosthenes(0), [])
        self.assertEqual(sieve_of_eratosthenes(1), [])
        self.assertEqual(sieve_of_eratosthenes(-123), [[3, 1], [41, 1]])
        self.assertEqual(sieve_of_eratosthenes(123), [[3, 1], [41, 1]])
        self.assertEqual(sieve_of_eratosthenes(562), [[2, 1], [281, 1]])
        self.assertEqual(sieve_of_eratosthenes(12), [[2, 2], [3, 1]])

    def test_performance(self):
        print(sieve_of_eratosthenes(453526297733342))


if '__main__' == __name__:
    unittest.main()
