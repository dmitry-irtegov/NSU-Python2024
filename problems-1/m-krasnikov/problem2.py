import unittest


def trim_sequence(sequence, lower_bound, upper_bound):
    trimmed_sequence = [min(max(num, lower_bound), upper_bound) for num in
                        sequence]
    return trimmed_sequence


class TestTrimSequenceFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(trim_sequence([], 1, 2), [])

    def test_zeros_list(self):
        self.assertEqual(trim_sequence([0, 0, 0], -1, 2), [0, 0, 0])

    def test_normal_case(self):
        self.assertEqual(trim_sequence([1, 2, 3, 4, 5, 6, 7], 3, 5),
                         [3, 3, 3, 4, 5, 5, 5])

    def test_unsorted_case(self):
        self.assertEqual(trim_sequence([-10, 56, 3, 4, -6, 8, 0], -3, 5),
                         [-3, 5, 3, 4, -3, 5, 0])

    def test_wrong_case(self):
        self.assertEqual(trim_sequence([3, 2, -56, 45, 10, -1, 0, 1], 5, 3),
                         [3, 3, 3, 3, 3, 3, 3, 3])


if __name__ == '__main__':
    unittest.main()
