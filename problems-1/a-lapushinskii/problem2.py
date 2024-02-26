import unittest

def cut_fun(numbers, min_border, max_border):
    for i, v in enumerate(numbers):
        numbers[i] = min(max(v, min_border), max_border)
    return numbers


class TestCutFunction(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(cut_fun([1, 2, 3], 1, 3), [1, 2, 3])
    def test_min(self):
        self.assertEqual(cut_fun([1, 2, 3], 2, 3), [2, 2, 3])
    def test_max(self):
        self.assertEqual(cut_fun([1, 2, 3], 1, 2), [1, 2, 2])
    def test_ficha(self):
        self.assertEqual(cut_fun([1, 2, 3], 3, 2), [2, 2, 2])
    def test_zero(self):
        self.assertEqual(cut_fun([], 3, 2), [])

if __name__ == "__main__":
  unittest.main()
