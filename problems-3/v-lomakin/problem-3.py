import math
import unittest

class Vector:
    def __init__(self,args):
        self.__args = args
        self.__size = len(args)
        
    def getList(self):
        return self.__args
        
    def len(self):
        sum = 0
        for i in self.__args:
            sum += i**2
        return math.sqrt(sum)
    
    def toString(self):
        res = "("
        for i in self.__args:
            res += str(i) + ", "
        res = res[:-2] + ")"
        return res
    
    def get(self, i):
        return self.__args[i]

    def nMult(self, n):
        return tuple([n*i for i in self.__args])

    def plus(self, vec):
        return tuple([a+b for a, b in zip(vec.getList(), self.__args)])

    def minus(self, vec):
        return tuple([a-b for a, b in zip(self.__args, vec.getList())])

    def mult(self, vec):
        return tuple([a*b for a, b in zip(vec.getList(), self.__args)])

    def equal(self, vec):
        flag = True
        if len(vec.getList()) != self.__size:
            return False
        for a, b in zip(vec.getList(), self.__args):
            if a != b:
                flag = False
        return flag

class TestVector (unittest.TestCase):
    def setUp(self):
        self.vector1 = Vector((1,2,3,4,5))
        self.vector2 = Vector((1,3,4,7,10))
        self.vector3 = Vector((1,2,3,4,5))
        self.vectorBigger = Vector((1,1,1,1,1,1,1,1,1))

    def test_len(self):
        self.assertEqual(self.vector1.len(), 7.416198487095663)

    def test_str(self):
        self.assertEqual(self.vector1.toString(), "(1, 2, 3, 4, 5)")
        
    def test_get(self):
        self.assertEqual(self.vector2.get(3), 7)

    def test_nMult(self):
        self.assertEqual(self.vector2.nMult(3), (3, 9, 12, 21, 30))

    def test_plus(self):
        self.assertEqual(self.vector1.plus(self.vector2), (2, 5, 7, 11, 15))

    def test_minus(self):
        self.assertEqual(self.vector1.minus(self.vector2), (0, -1, -1, -3, -5))

    def test_mult(self):
        self.assertEqual(self.vector1.mult(self.vector2), (1, 6, 12, 28, 50))

    def test_equal(self):
        self.assertTrue(self.vector1.equal(self.vector3))
        self.assertFalse(self.vector1.equal(self.vector2))
        self.assertFalse(self.vector1.equal(self.vectorBigger))
    
        
if __name__ == "__main__":
  unittest.main()


