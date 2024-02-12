import unittest


def trim_sequence(numbers: list, a, b):
    if a > b:
        raise ArithmeticError("a is greater than b")
    for i, num in enumerate(numbers):
        numbers[i] = min(max(num, a), b)


class TestTrimSequence(unittest.TestCase):
    def test_trim_sequence(self):
        seq = [0, 1, 3, 4, 5, 0]
        trim_sequence(seq, 2, 4)
        self.assertEqual(seq, [2, 2, 3, 4, 4, 2])
        seq = []
        trim_sequence(seq, 0, 0)
        self.assertEqual(seq, [])
        with self.assertRaises(ArithmeticError):
            trim_sequence([0, 1, 2, 3], 3, 0)


if __name__ == '__main__':
    unittest.main()
