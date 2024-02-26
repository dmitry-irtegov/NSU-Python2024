import unittest

def cut(list, a, b):
     if a > b:
          a,b = b,a
     return [max(min(i, b), a) for i in list]

class TestFirstTask(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(cut([1,2,3,4,5,6,7,8,9,10,11],3,7),[3,3,3,4,5,6,7,7,7,7,7])

    def test_nothing(self):
        self.assertEqual(cut([],4,6),[])

    def test_null(self):
        self.assertEqual(cut([0],4,7),[4])

    def test_uncorrect(self):
        self.assertEqual(cut([1,5,9,15],10,3),[3,5,9,10])

if __name__ == '__main__':
    unittest.main()
