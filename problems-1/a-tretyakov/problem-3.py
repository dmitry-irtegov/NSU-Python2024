import unittest


def collatz_hypothesis(num, chain=None):
    if chain is None:
        chain = [num]

    if num == 0:
        raise ValueError("Number doesn't satisfies Collatz hypothesis")
    if num == 1:
        return chain

    num = num // 2 if num % 2 == 0 else num * 3 + 1
    return collatz_hypothesis(num, [*chain, num])


class TestCollatzHypothesis(unittest.TestCase):

    def test_simple_case(self):
        self.assertEquals([3, 10, 5, 16, 8, 4, 2, 1], collatz_hypothesis(3))

    def test_big_number(self):
        self.assertEquals(
            [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            collatz_hypothesis(9)
        )

    def test_one(self):
        self.assertEquals([1], collatz_hypothesis(1))

    def test_zero(self):
        self.assertRaises(ValueError, collatz_hypothesis, 0)


if __name__ == "__main__":
    unittest.main()
