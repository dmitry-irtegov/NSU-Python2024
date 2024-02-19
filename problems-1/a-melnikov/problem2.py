import unittest


def cut_list(seq: list[float], lo: float, hi: float) -> list[float]:
    return [elem if lo <= elem <= hi else lo if elem < lo else hi for elem in seq]


class TestCutList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(cut_list([], 1, 5), [])

    def test_not_cut(self):
        self.assertEqual(cut_list([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_common(self):
        self.assertEqual(
            cut_list([1.2, 2.3, 3.4, 4.5, 6, 7, 8, 8.9], 2.4, 7.9),
            [2.4, 2.4, 3.4, 4.5, 6, 7, 7.9, 7.9],
        )

if __name__ == '__main__':
    unittest.main()
