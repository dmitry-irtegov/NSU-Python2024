import unittest


def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


class TestTrimSequenceFunction(unittest.TestCase):
    def test_one(self):
        self.assertEqual(collatz_sequence(1), [1])

    def test_big_number(self):
        self.assertEqual(collatz_sequence(79),
                         [79, 238, 119, 358, 179, 538, 269,
                          808, 404, 202, 101, 304, 152, 76,
                          38, 19, 58, 29, 88, 44, 22, 11, 34,
                          17, 52, 26, 13, 40, 20, 10, 5, 16,
                          8, 4, 2, 1])

    def test_small_number(self):
        self.assertEqual(collatz_sequence(9),
                         [9, 28, 14, 7, 22, 11, 34, 17, 52,
                          26, 13, 40, 20, 10, 5, 16, 8, 4,
                          2, 1])


if __name__ == "__main__":
    unittest.main()
