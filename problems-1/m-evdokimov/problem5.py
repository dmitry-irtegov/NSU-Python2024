import unittest

def factorization(n):

    i = 2
    resList = []
    
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            cnt = cnt + 1
            n = n // i
        if cnt != 0:
            resList.append([i, cnt])
        i = i + 1
        
    if n > 1:
        resList.append([n, 1])
            
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
