import unittest


def collatz_conjecture(n):
    chain = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        chain.append(n)
    return chain


class TestCollatzConjecture(unittest.TestCase):

    def test_input_1(self):
        self.assertEqual(collatz_conjecture(1), [1])

    def test_input_10(self):
        self.assertEqual(collatz_conjecture(10), [10, 5, 16, 8, 4, 2, 1])

    def test_input_20(self):
        self.assertEqual(collatz_conjecture(20), [20, 10, 5, 16, 8, 4, 2, 1])

    def test_input_100(self):
        self.assertEqual(collatz_conjecture(100),
                         [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4,
                          2, 1])


if __name__ == '__main__':
    unittest.main()
