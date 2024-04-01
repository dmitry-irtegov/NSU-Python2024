import unittest


def border_func(x, a, b):
    return a if x < a else b if x > b else x


def cut_elements(l, a, b):
    return [border_func(x, a, b) for x in l]


class TestForCutFunction(unittest.TestCase):
    def test_with_positive_numbers(self):
        self.assertEqual([2, 3, 5, 6, 6], cut_elements([1, 3, 5, 7, 9], 2, 6))

    def test_with_empty_list(self):
        self.assertEqual([], cut_elements([], 2, 6))

    def test_with_swap_borders(self):
        self.assertEqual([6, 6, 6, 2, 2], cut_elements([1, 3, 5, 7, 9], 6, 2))

    def test_with_mixed_list(self):
        self.assertEqual([1, -1, 6, 7, -1, 8, 8], cut_elements([1, -3, 6, 7, -10, 9, 50], -1, 8))


if __name__ == '__main__':
    unittest.main()
