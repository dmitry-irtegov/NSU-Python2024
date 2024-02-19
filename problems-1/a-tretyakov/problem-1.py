from functools import reduce
import unittest


def cumulative_sum(data):
    return reduce(lambda acc, x: [*acc, acc[-1] + x], data, [0])


class TestCumulativeSum(unittest.TestCase):
    def test_example_list(self):
        self.assertEqual([0, 1, 3, 6], cumulative_sum([1, 2, 3]))

    def test_empty_list(self):
        self.assertEqual([0], cumulative_sum([]))

    def test_zero_list(self):
        self.assertEqual([0, 0, 0, 0], cumulative_sum([0, 0, 0]))

    def test_negative_numbers_list(self):
        self.assertEqual([0, -1, -3, -6], cumulative_sum([-1, -2, -3]))


if __name__ == "__main__":
    unittest.main()
