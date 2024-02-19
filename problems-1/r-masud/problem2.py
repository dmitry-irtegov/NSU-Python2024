import unittest

def cut_numbers(numbers, a, b):
    modified_numbers = [0]*len(numbers)

    for i, num in enumerate(numbers):
        if num < a:
            modified_numbers[i] = a
        elif num > b:
            modified_numbers[i] = b
        else:
            modified_numbers[i]= num
    return modified_numbers

class TestCutNumbers(unittest.TestCase):
    def test_cut_numbers_case1(self):
        self.assertEqual(cut_numbers([2, 5, 8, 12, 15, 18], 6, 14), [6, 6, 8, 12, 14, 14])

    def test_cut_numbers_case2(self):
        self.assertEqual(cut_numbers([-10, -5, -2, 0, 5], -7, 3), [-7, -5, -2, 0, 3])

    def test_cut_numbers_case3(self):
        self.assertEqual(cut_numbers([-3, -1, 0, 2, 4], -2, 3), [-2, -1, 0, 2, 3])

    def test_cut_numbers_case4(self):
        self.assertEqual(cut_numbers([], 0, 100), [])

if __name__ == '__main__':
    unittest.main()