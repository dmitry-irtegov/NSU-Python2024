import unittest

def my_find(l, number):
    for index, sub_list in enumerate(l):
        if sub_list[0] == number:
            return index
    return -1

def factorization(n):

    i = 2
    resList = []
    
    while i * i <= n:
        while n % i == 0:
            index = my_find(resList, i)
            if index != -1 :
                resList[index][1] = resList[index][1] + 1
            else:
                resList.append([i, 1])
            n = n // i
        i = i + 1
        
    if n > 1:
        index = my_find(resList, n)
        if index != -1:
            resList[index][1] = resList[index][1] + 1
        else:
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
