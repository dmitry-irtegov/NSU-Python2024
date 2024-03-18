import unittest


def cumulative_sums(nums):
    sum = 0
    result = [0] * (len(nums) + 1)
    result[0] = sum
    for idx, num in enumerate(nums):
        sum += num
        result[idx + 1] = sum
    return result


class TestCumulativeSums(unittest.TestCase):

    def test(self):
        self.assertEqual(cumulative_sums([1, 2, 3]), [0, 1, 3, 6])
        self.assertEqual(cumulative_sums([5, 6, 1]), [0, 5, 11, 12])


if '__main__' == __name__:
    unittest.main()
