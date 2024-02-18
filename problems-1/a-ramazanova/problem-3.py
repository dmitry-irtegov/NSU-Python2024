import unittest


def collatz(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            result.append(n)
        else:
            n = 3 * n + 1
            result.append(n)
    print(" -> ".join(f"{x:.0f}" for x in result))
    return result


class TestCollatz(unittest.TestCase):
    def test_collatz_sequence_3(self):
        expected_sequence = [3, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(collatz(3), expected_sequence)

    def test_collatz_sequence_20(self):
        expected_sequence = [20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(collatz(20), expected_sequence)

    def test_collatz_sequence_1(self):
        expected_sequence = [1]
        self.assertEqual(collatz(1), expected_sequence)


if __name__ == '__main__':
    unittest.main()