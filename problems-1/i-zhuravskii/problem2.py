import unittest


def list_cut(numbers, lower_border, upper_border):
    return [lower_border if num < lower_border
            else upper_border if num > upper_border
    else num for num in numbers]


class TestListCut(unittest.TestCase):
    def test_list_cut_1(self):
        self.assertEquals(list_cut([1, 2, 3, 4, 5], 1, 5), [1, 2, 3, 4, 5])

    def test_list_cut_2(self):
        self.assertEquals(list_cut([1, 2, 3, 4, 5], 2, 4), [2, 2, 3, 4, 4])

    def test_list_cut_3(self):
        self.assertEquals(list_cut([1, 2, 3, 4, 5], 1, 2), [1, 2, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()

