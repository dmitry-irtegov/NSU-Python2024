from sys import maxsize
import unittest

def cumulative_sum(seq):
    result = [0] * (len(seq) + 1)
    for i in range(0, len(seq) + 1):
        result[i] = sum(seq[0:i])
    return result

class TestCumulativeSum(unittest.TestCase):
    
    def test_zeros(self):
        print(cumulative_sum([0, 0, 0]))
        self.assertEqual(cumulative_sum([0, 0, 0]), [0, 0, 0, 0]) 

    def test_simple(self):
        print(cumulative_sum([1, 2, 3]))
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6]) 
    
    def test_ones(self):
        print(cumulative_sum([1, 1, 1]))
        self.assertEqual(cumulative_sum([1, 1, 1]), [0, 1, 2, 3]) 
    
    def test_float(self):
        print(cumulative_sum([0.5, -0.36, 3.1456]))
        self.assertEqual(cumulative_sum([0.5, -0.36, 3.1456]), [0, 0.5, 0.14, 3.2856]) 
    
    def test_maxsize_plus(self):
        print(cumulative_sum([maxsize, 2, 3]))
        self.assertEqual(cumulative_sum([maxsize, 2, 3]), [0, maxsize, maxsize + 2, maxsize + 2 + 3])

if __name__ == '__main__':
    unittest.main()
