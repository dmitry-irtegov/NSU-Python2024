import unittest


def cumulative_sum(input_list):
    result = [0] * (len(input_list) + 1)
    for i, number in enumerate(input_list, 0):
        result[i + 1] = result[i] + number
    return result


class TestCumulativeSum(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_positive_numbers(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])

    def test_negative_numbers(self):
        self.assertEqual(cumulative_sum([-1, -2, -3]), [0, -1, -3, -6])

    def test_mixed_numbers(self):
        self.assertEqual(cumulative_sum([1, -2, 3, -4, 5, -6]), [0, 1, -1, 2, -2, 3, -3])


if __name__ == '__main__':
    unittest.main()
