import unittest

def limiter(inputList, a, b):

    inputList = inputList.split()

    resultList = [None] * len(inputList)
    for index, number in enumerate(inputList):
        x = int(number)
        if x > b:
            x = b
        if x < a:
            x = a
        resultList[index] = x
    
    return resultList

class TestLimiter(unittest.TestCase):
  
    def test_12345_2_4(self):
        self.assertEqual(limiter("1 2 3 4 5", 2, 4), [2, 2, 3, 4, 4])
    
    def test_1_0_1(self):
        self.assertEqual(limiter("1 0", 0, 1), [1, 0])
        
    def test_090_1_2(self):
        self.assertEqual(limiter("0 9 0", 1, 2), [1, 2, 1])
        
    def test_error_test(self):
        with self.assertRaises(ValueError):
            limiter("a b c", 1, 2)
  
if __name__ == "__main__":
  unittest.main()