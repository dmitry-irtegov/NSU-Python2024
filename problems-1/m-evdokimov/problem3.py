import unittest

test_output = []

def custom_print(*ins, **args):
    num = ins[0]
    test_output.append(num)

def theory(a):
    
    while a != 1:
        print(a, ' -> ',  end = '', sep ='') 
        if a % 2 == 0:
            a = a//2
        else:
            a = 3 * a + 1
    print(1)


class TestTheory(unittest.TestCase):
    
    def setUp(self):
        global print
        self.orig_print = print
        print = custom_print
        test_output.clear()
        
    def tearDown(self):
        global print
        print = self.orig_print
  
    def test_5(self):
        theory(5)
        self.assertEqual(test_output, [5, 16, 8, 4, 2, 1])
    
    def test_1(self):
        theory(1)
        self.assertEqual(test_output, [1])
        
    def test_10(self):
        theory(10)
        self.assertEqual(test_output, [10, 5, 16, 8, 4, 2, 1])
  
if __name__ == "__main__":
    unittest.main()