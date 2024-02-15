import unittest


def calculate_cumulative_sum(l):
    return [sum(l[:i]) for i in range(len(l) + 1)]


class TestCumulativeSum(unittest.TestCase):
    def test_init_condition(self):
        self.assertEqual([0, 1, 3, 6], calculate_cumulative_sum([1, 2, 3]))

    def test_empty_list(self):
        self.assertEqual([0], calculate_cumulative_sum([]))

    def test_negative_numbers_list(self):
        self.assertEqual([0, -1, -3, -6], calculate_cumulative_sum([-1, -2, -3]))


if __name__ == '__main__':
    unittest.main()
