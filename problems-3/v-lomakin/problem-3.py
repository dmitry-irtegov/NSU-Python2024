import math
import unittest

class Vector:
    def __init__(self,args):
        self.args = args
        self.size = len(args)
        
    def getList(self):
        return self.args
        
    def len(self):
        sum = 0
        for i in self.args:
            sum += i**2
        return math.sqrt(sum)
    
    def toString(self):
        res = "("
        for i in self.args:
            res += str(i) + ", "
        res = res[:-2] + ")"
        return res
    
    def get(self, i):
        return self.args[i]

    def nMult(self, n):
        self.args = [n*i for i in self.args]

    def plus(self, vec):
        for i in range(self.size):
            self.args[i] += vec.get(i)

    def minus(self, vec):
        for i in range(self.size):
            self.args[i] -= vec.get(i)

    def mult(self, vec):
        for i in range(self.size):
            self.args[i] *= vec.get(i)

    def equal(self, vec):
        flag = True
        for i in range(self.size):
            if self.args[i] != vec.get(i):
                flag = False
        return flag

class TestVector (unittest.TestCase):
    def setUp(self):
        self.vector1 = Vector([1,2,3,4,5])
        self.vector2 = Vector([1,3,4,7,10])
        self.vector3 = Vector([1,2,3,4,5])

    def test_len(self):
        self.assertEqual(self.vector1.len(), 7.416198487095663)

    def test_str(self):
        self.assertEqual(self.vector1.toString(), "(1, 2, 3, 4, 5)")
        
    def test_get(self):
        self.assertEqual(self.vector2.get(3), 7)

    def test_nMult(self):
        self.vector2.nMult(3)
        self.assertEqual(self.vector2.getList(), [3, 9, 12, 21, 30])

    def test_plus(self):
        self.vector1.plus(self.vector2)
        self.assertEqual(self.vector1.getList(), [2, 5, 7, 11, 15])

    def test_minus(self):
        self.vector1.minus(self.vector2)
        self.assertEqual(self.vector1.getList(), [0, -1, -1, -3, -5])

    def test_mult(self):
        self.vector1.mult(self.vector2)
        self.assertEqual(self.vector1.getList(), [1, 6, 12, 28, 50])

    def test_equal(self):
        self.assertTrue(self.vector1.equal(self.vector3))
        self.assertFalse(self.vector1.equal(self.vector2))
    
        
if __name__ == "__main__":
  unittest.main()


