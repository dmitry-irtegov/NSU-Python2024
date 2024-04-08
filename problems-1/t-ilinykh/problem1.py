import unittest

def cumulative_sum(arr):
    cumm_sum = [0]

    for i in range(len(arr)):
        cumm_sum.append(cumm_sum[i]+arr[i])

    return cumm_sum

class TestCumulative(unittest.TestCase):
    def test_three(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])
    def test_four(self):
        self.assertEqual(cumulative_sum([3, 2, 3, 2]), [0, 3, 5, 8, 10])
    def test_one(self):
        self.assertEqual(cumulative_sum([1]), [0, 1])
    def test_zero(self):
        self.assertEqual(cumulative_sum([]), [0])

if __name__ == '__main__':
    unittest.main()
