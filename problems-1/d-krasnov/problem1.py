import unittest


def cumulative_sums(numbers):
    result = [0] * (len(numbers) + 1)
    total = 0
    for i, num in enumerate(numbers):
        total += num
        result[i + 1] = total
    return result


class TestCumulativeSums(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual([0], cumulative_sums([]))

    def test_positive_numbers(self):
        self.assertEqual([0, 1, 3, 6], cumulative_sums([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertEqual([0, -1, -3, -6], cumulative_sums([-1, -2, -3]))

    def test_mixed_numbers(self):
        self.assertEqual([0, 1, -1, 2, -2], cumulative_sums([1, -2, 3, -4]))

    def test_single_number(self):
        self.assertEqual([0, 5], cumulative_sums([5]))


if __name__ == '__main__':
    unittest.main()
