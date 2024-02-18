import unittest


def cut_numbers(numbers, a, b):
    if a > b:
        return
    return [min(max(num, a), b) for num in numbers]


class TestCutNumbers(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(cut_numbers([], 2, 3), [])

    def test_no_borders(self):
        self.assertEqual(cut_numbers([1, 2, 3], 1, 3), [1, 2, 3])

    def test_wrong_borders(self):
        self.assertEqual(cut_numbers([1, 2, 3], 10, 0), None)

    def test_borders(self):
        self.assertEqual(cut_numbers([0, 20, 40], 10, 30), [10, 20, 30])


if __name__ == '__main__':
    unittest.main()
