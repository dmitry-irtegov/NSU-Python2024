import unittest
from numpy.testing import assert_almost_equal

def cumulative_sum(array):
    c_arr = [0] * (len(array) + 1)
    for i in range(0, len(array)):
        c_arr[i+1] = c_arr[i] + array[i]

    return c_arr

class TestCumulativeSum(unittest.TestCase):
    def test_example(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])

    def test_negative_numbers(self):
        self.assertEqual(cumulative_sum([-1, -2, -3]), [0, -1, -3, -6])

    def test_alt_signs(self):
        self.assertEqual(cumulative_sum([-1, 0, 1]), [0, -1, -1, 0])

    def test_floats(self):
        assert_almost_equal(cumulative_sum([-1.2, 0.3, 1.4]), [0, -1.2, -0.9, 0.5])

    def test_empty_input(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_single_number(self):
        self.assertEqual(cumulative_sum([5]), [0, 5])

if __name__ == '__main__':
    unittest.main()