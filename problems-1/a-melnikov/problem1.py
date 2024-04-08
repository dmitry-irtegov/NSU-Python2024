import unittest


def cumulative_sum(seq: list) -> list:
    sum = 0
    return [0] + [(sum := sum + elem) for elem in seq]


class TestCumulativeSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_positive_numbers(self):
        self.assertEqual(
            cumulative_sum([15, 3, 987, 4, 1, 0, 3]),
            [0, 15, 18, 1005, 1009, 1010, 1010, 1013],
        )

    def test_integers(self):
        self.assertEqual(cumulative_sum([15, 0, -15, -3, 4]), [0, 15, 15, 0, -3, 1])


if __name__ == "__main__":
    unittest.main()
