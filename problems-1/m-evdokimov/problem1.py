import unittest

def cumulativeSum(inputList):

    length = len(inputList)
    resultList = [None] * (length + 1)
    resultList[0] = 0

    for index, number in enumerate(inputList):
        resultList[index+1] = resultList[index] + number
    
    return resultList

class TestCumulativeSum(unittest.TestCase):
  
    def test_123(self):
        self.assertEqual(cumulativeSum([1, 2, 3]), [0, 1, 3, 6])
    
    def test_1(self):
        self.assertEqual(cumulativeSum([1]), [0, 1])
        
    def test_below_zero(self):
        self.assertEqual(cumulativeSum([-1, -2, -3]), [0, -1, -3, -6])
        
    def test_exception(self):
        with self.assertRaises(TypeError):
            cumulativeSum(['a', 'b', 'c'])
  
if __name__ == "__main__":
  unittest.main()
