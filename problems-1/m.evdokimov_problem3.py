import unittest

def theory(a):
    
    resultList = []
    while a != 1:
        resultList.append(a)
        if a % 2 == 0:
            a = a//2
        else:
            a = 3 * a + 1
    resultList.append(1)        
    return resultList

class TestTheory(unittest.TestCase):
  
    def test_5(self):
        self.assertEqual(theory(5), [5, 16, 8, 4, 2, 1])
    
    def test_1(self):
        self.assertEqual(theory(1), [1])
        
    def test_10(self):
        self.assertEqual(theory(10), [10, 5, 16, 8, 4, 2, 1])
  
if __name__ == "__main__":
  unittest.main()

