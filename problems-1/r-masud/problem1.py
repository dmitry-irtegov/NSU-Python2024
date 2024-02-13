import unittest

def cumulative_sums(seq):
    cum = [0]
    total_sum = 0

    for num in seq:
        total_sum += num
        cum.append(total_sum)
    return cum

class TestCumulativeSums(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3], [0, 1, 3, 6]),
            ([3, 4, 5, 6], [0, 3, 7, 12, 18]),
            ([-1, -2, -3], [0, -1, -3, -6]),
            ([1, -2, 3, -4, 5], [0, 1, -1, 2, -2, 3])
        ]
    def test_cumulative_sums(self):
        for seq, expected in self.test_cases:
                with self.subTest(seq=seq):
                    result = cumulative_sums(seq)
                    self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
