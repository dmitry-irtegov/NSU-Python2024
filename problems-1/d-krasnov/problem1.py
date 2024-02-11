import unittest


def cumulative_sums(numbers):
    result = [0]
    total = 0
    for num in numbers:
        total += num
        result.append(total)
    return result


class TestCumulativeSums(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(cumulative_sums([]), [0])

    def test_positive_numbers(self):
        self.assertEqual(cumulative_sums([1, 2, 3]), [0, 1, 3, 6])

    def test_negative_numbers(self):
        self.assertEqual(cumulative_sums([-1, -2, -3]), [0, -1, -3, -6])

    def test_mixed_numbers(self):
        self.assertEqual(cumulative_sums([1, -2, 3, -4]), [0, 1, -1, 2, -2])

    def test_single_number(self):
        self.assertEqual(cumulative_sums([5]), [0, 5])


if __name__ == '__main__':
    unittest.main()
