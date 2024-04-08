import unittest


def clamp_values(input_list, a, b):
    for i, number in enumerate(input_list):
        if number < a:
            input_list[i] = a
        elif number > b:
            input_list[i] = b
    return input_list


class TestClampValues(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(clamp_values([1, 2, 3, 4, 5], 2, 4), [2, 2, 3, 4, 4])

    def test_empty_list(self):
        self.assertEqual(clamp_values([], 2, 4), [])

    def test_negative_values(self):
        self.assertEqual(clamp_values([-5, -3, 0, 2, 6], -4, 4), [-4, -3, 0, 2, 4])

    def test_same_a_and_b(self):
        self.assertEqual(clamp_values([1, 2, 3, 4, 5], 3, 3), [3, 3, 3, 3, 3])


if __name__ == '__main__':
    unittest.main()
