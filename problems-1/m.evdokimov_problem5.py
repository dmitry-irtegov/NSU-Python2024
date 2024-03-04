import unittest

def factorization(n):

    i = 2
    resList = []
    
    while i * i <= n:
        while n % i == 0:
            resList.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        resList.append(n)
    
    setList = set(resList)
    final = []
    
    for i in setList:
        final.append([i, resList.count(i)])
    
    return final

class TestFactorization(unittest.TestCase):
  
    def test_2(self):
        self.assertEqual(factorization(2), [[2, 1]])
    
    def test_12(self):
        self.assertEqual(factorization(12), [[2, 2], [3, 1]])
        
    def test_109(self):
        self.assertEqual(factorization(109), [[109, 1]])
  
if __name__ == "__main__":
  unittest.main()

