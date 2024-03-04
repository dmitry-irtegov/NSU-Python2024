# problems-1/assignment-1
import unittest


def cumulative_sum(arr):
    ans = [0] * (len(arr) + 1)
    for i, v in enumerate(arr, start=1):
        ans[i] = ans[i - 1] + v
    return ans


class CumulativeSum(unittest.TestCase):
    def test_init(self):
        self.assertEqual([0, 1, 3, 6], cumulative_sum([1, 2, 3]))

    def test_empty_list(self):
        self.assertEqual([0], cumulative_sum([]))

    def test_negative_numbers_list(self):
        self.assertEqual([0, -1, -3, -6], cumulative_sum([-1, -2, -3]))


if __name__ == '__main__':
    unittest.main()
