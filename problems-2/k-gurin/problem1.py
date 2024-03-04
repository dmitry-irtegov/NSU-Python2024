# problems-2/assignment-1
import unittest


def pythagorean_threes(n):
    return [(x, y, z) for x in range(n)
            for y in range(x, n)
            for z in range(y, n)
            if x ** 2 + y ** 2 == z ** 2]


class PythagoreanThrees(unittest.TestCase):
    def test_init(self):
        self.assertEqual([(0, 0, 0), (0, 1, 1), (0, 2, 2)], pythagorean_threes(3))

    def test_empty_list(self):
        self.assertEqual([], pythagorean_threes(0))

    def test_one_element(self):
        self.assertEqual([(0, 0, 0)], pythagorean_threes(1))


if __name__ == '__main__':
    unittest.main()
