# problems-1/assignment-3
import unittest


def collatz_hypothesis(n):
    trans_chain = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        trans_chain.append(n)
    return trans_chain


class CollatzHypothesis(unittest.TestCase):
    def test_init(self):
        self.assertEqual([3, 10, 5, 16, 8, 4, 2, 1], collatz_hypothesis(3))

    def test_even(self):
        self.assertEqual([2, 1], collatz_hypothesis(2))

    def test_odd(self):
        self.assertEqual([5, 16, 8, 4, 2, 1], collatz_hypothesis(5))


if __name__ == '__main__':
    unittest.main()
