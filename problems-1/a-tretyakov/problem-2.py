import unittest


def trim_list(data, lower_bound, upper_bound):
    def trim_fn(elem, lb, ub):
        return lb if elem < lb else ub

    allocated_arr = [0] * len(data)

    for index, value in enumerate(data):
        allocated_arr[index] = trim_fn(value, lower_bound, upper_bound)

    return allocated_arr


class TestTrimList(unittest.TestCase):

    def test_sample_case(self):
        self.assertEquals([5, 12, 12, 5], trim_list([4, 13, 25, 1], 5, 12))

    def test_lower_numbers(self):
        self.assertEquals([0, 0, 0, 0], trim_list([-1, -2, -3, -4], 0, 100))

    def test_bigger_numbers(self):
        self.assertEquals([15, 15, 15, 15], trim_list([20, 2000, 20000, 2000000], 0, 15))


if __name__ == "__main__":
    unittest.main()
