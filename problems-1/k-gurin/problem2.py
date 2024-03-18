# problems-1/assignment-2
import unittest


def cut_numbers(arr, a, b):
    for i in range(len(arr)):
        if arr[i] < a:
            arr[i] = a
        elif arr[i] > b:
            arr[i] = b
    return arr


class TestForCutFunction(unittest.TestCase):
    def test_with_positive_numbers(self):
        self.assertEqual([2, 3, 5, 6, 6], cut_numbers([1, 3, 5, 7, 9], 2, 6))

    def test_with_empty_list(self):
        self.assertEqual([], cut_numbers([], 2, 6))

    def test_with_swap_borders(self):
        self.assertEqual([6, 6, 6, 2, 2], cut_numbers([1, 3, 5, 7, 9], 6, 2))

    def test_with_mixed_list(self):
        self.assertEqual([1, -1, 6, 7, -1, 8, 8], cut_numbers([1, -3, 6, 7, -10, 9, 50], -1, 8))


if __name__ == '__main__':
    unittest.main()
