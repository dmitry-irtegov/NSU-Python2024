
def sum_cumulative (arr):
    result = [0] * (len(arr)+1)
    for i, x in enumerate(arr):
        result[i+1] = result[i] + x
    return result

print(sum_cumulative([1, 2, 3]))

###

import unittest

class TestCumulativeSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_cumulative([1, 2, 3]), [0, 1, 3, 6])
    def test_more(self):
        self.assertEqual(sum_cumulative([1, 2, 3, 4, 5, 6, 7]), [0, 1, 3, 6, 10, 15, 21, 28])


if __name__ == '__main__':
    unittest.main()
