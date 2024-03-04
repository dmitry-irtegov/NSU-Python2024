import unittest

def cum_sum(input):
    N = len(input)
    res = [0]*(len(input)+1)
    for i in range(1, N+1):
        res[i] = res[i-1] + input[i-1]
    return res

class TestCumSumFunction(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(cum_sum([]), [0])

    def test_single_element(self):
        self.assertEqual(cum_sum([10]), [0,10])

    def test_simple_input(self):
        self.assertEqual(cum_sum([1,2,3,4]), [0,1,3,6,10])

    def test_negative_input(self):
        self.assertEqual(cum_sum([1, -1, 1, -1]), [0, 1, 0, 1, 0])

if __name__ == '__main__':
    unittest.main()
