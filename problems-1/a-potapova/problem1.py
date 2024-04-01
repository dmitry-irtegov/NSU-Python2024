import unittest


def cum_sum_sequence(numbers: list) -> list:
    result = [0]
    for i, num in enumerate(numbers):
        result.append(result[i] + num)
    return result


class TestCumSumSequence(unittest.TestCase):
    def test_cum_sum_sequence(self):
        res = cum_sum_sequence([1, 2, 3])
        self.assertEqual(res, [0, 1, 3, 6])
        res = cum_sum_sequence([])
        self.assertEqual(res, [0])


if __name__ == '__main__':
    unittest.main()
