import unittest


def clamp_values(input_list, a, b):
    result = []
    for i in input_list:
        if i < a:
            result.append(a)
        elif i > b:
            result.append(b)
        else:
            result.append(i)
    return result


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
