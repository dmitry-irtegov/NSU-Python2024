import unittest


def cumulative_sum(input_list):
    s = 0
    result = [s]
    for i in input_list:
        s += i
        result.append(s)
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
