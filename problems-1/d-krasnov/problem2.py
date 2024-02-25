import unittest


def cut_numbers(numbers, a, b):
    return [min(max(num, a), b) for num in numbers]


class TestCutNumbers(unittest.TestCase):
    def test_cut_numbers_case1(self):
        self.assertEqual(cut_numbers([1, 2, 3], 1, 3), [1, 2, 3])

    def test_cut_numbers_case2(self):
        self.assertEqual(cut_numbers([1, 2, 3], 2, 3), [2, 2, 3])

    def test_cut_numbers_case3(self):
        self.assertEqual(cut_numbers([1, 2, 3], 1, 2), [1, 2, 2])


if __name__ == "__main__":
    unittest.main()
