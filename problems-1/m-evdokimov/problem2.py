import unittest

def limiter(inputList, a, b):

    resultList = [None] * len(inputList)
    for index, number in enumerate(inputList):
        
        if number > b:
            number = b
        if number < a:
            number = a
        resultList[index] = number
    
    return resultList

class TestLimiter(unittest.TestCase):
  
    def test_12345_2_4(self):
        self.assertEqual(limiter([1, 2, 3, 4, 5], 2, 4), [2, 2, 3, 4, 4])
    
    def test_1_0_1(self):
        self.assertEqual(limiter([1, 0], 0, 1), [1, 0])
        
    def test_090_1_2(self):
        self.assertEqual(limiter([0, 9, 0], 1, 2), [1, 2, 1])
        
    def test_error_test(self):
        with self.assertRaises(TypeError):
            limiter(['a', 'b', 'c'], 1, 2)
  
if __name__ == "__main__":
  unittest.main()