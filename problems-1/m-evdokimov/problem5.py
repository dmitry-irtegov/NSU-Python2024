import unittest

def factorization(n):

    i = 2
    resDict = {}
    
    while i * i <= n:
        while n % i == 0:
            if i in resDict :
                resDict[i] = resDict[i] + 1
            else:
                resDict[i] = 1
            n = n // i
        i = i + 1
        
    if n > 1:
        if n in resDict :
            resDict[n] = resDict[n] + 1
        else:
            resDict[n] = 1
            
    resList = []
    for key in resDict:
        resList.append([key, resDict[key]])
            
    return resList

class TestFactorization(unittest.TestCase):
  
    def test_2(self):
        self.assertEqual(factorization(2), [[2, 1]])
    
    def test_12(self):
        self.assertEqual(factorization(12), [[2, 2], [3, 1]])
        
    def test_109(self):
        self.assertEqual(factorization(109), [[109, 1]])
        
    def test_exeption(self):
        with self.assertRaises(TypeError):
            factorization("hello")
  
if __name__ == "__main__":
  unittest.main()
