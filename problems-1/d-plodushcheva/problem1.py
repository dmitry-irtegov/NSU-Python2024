import unittest


def cumulative_sum(numbers):
    res = [0]
    for number in numbers:
        res.append(res[-1] + number)
    return res


class TestCumulativeSum(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_one_number(self):
        self.assertEqual(cumulative_sum([3]), [0, 3])

    def test_three_numbers(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])

    def test_mixed_numbers(self):
        self.assertEqual(cumulative_sum([1, -2, 3]), [0, 1, -1, 2])


if __name__ == '__main__':
    unittest.main()
