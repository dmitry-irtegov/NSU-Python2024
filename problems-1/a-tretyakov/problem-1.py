import unittest


def cumulative_sum(data):
    allocated_arr = [0] * (len(data) + 1)
    for index in range(len(data) + 1):
        allocated_arr[index] = sum(data[:index])
    return allocated_arr


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
