from math import sqrt
import unittest


def factorize(x):
    ans = []
    for p in range(2, int(sqrt(x) + 1)):
        deg = 0
        while x % p == 0:
            deg += 1
            x = x // p
        if deg != 0:
            ans.append([p, deg])
    if x > 1:
        ans.append([x, 1])
    return ans


class TestFactorize(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(factorize(12), [[2, 2], [3, 1]])

    def test_big_number(self):
        self.assertEquals(factorize(123456789), [[3, 2], [3607, 1], [3803, 1]])

    def test_prime(self):
        self.assertEquals(factorize(7), [[7, 1]])


if __name__ == '__main__':
    unittest.main()
