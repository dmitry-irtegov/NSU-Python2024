import unittest


def cumulative_sum(sequence):
    return [sum(sequence[:i]) for i in range(len(sequence) + 1)]


class TestCumulativeSumFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_zeros(self):
        self.assertEqual(cumulative_sum([0, 0, 0]), [0, 0, 0, 0])

    def test_positive_numbers(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])

    def test_negative_numbers(self):
        self.assertEqual(cumulative_sum([-1, -2, -3]), [0, -1, -3, -6])

    def test_negative_and_positive_numbers(self):
        self.assertEqual(cumulative_sum([10, -5, 3, 7]), [0, 10, 5, 8, 15])


if __name__ == '__main__':
    unittest.main()
