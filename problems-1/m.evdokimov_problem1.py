import unittest

def cumulativeSum(inputList):

    inputList = inputList.split()

    l = len(inputList)
    resultList = [None] * (l + 1)
    resultList[0] = 0

    for i in range(l):
        resultList[i+1] = resultList[i] + int(inputList[i])
    
    return resultList

class TestCumulativeSum(unittest.TestCase):
  
    def test_123(self):
        self.assertEqual(cumulativeSum("1 2 3"), [0, 1, 3, 6])
    
    def test_1(self):
        self.assertEqual(cumulativeSum("1"), [0, 1])
        
    def test_000(self):
        self.assertEqual(cumulativeSum("0 0 0"), [0, 0, 0, 0])
  
if __name__ == "__main__":
  unittest.main()