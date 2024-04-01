import unittest

def cut(a, lower_limit, upper_limit):
    if upper_limit < lower_limit:
        raise ValueError("upper limit should be higher then lower limit")
    cutted = [0]*len(a)
    for i in range(len(a)):
        if a[i] > upper_limit:
            cutted[i] = upper_limit
        elif a[i] < lower_limit:
            cutted[i] = lower_limit
        else:
            cutted[i] = a[i] 
    return cutted

class TestCutFunction(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(cut([1,2,3,4,5,6,7,8], 2, 5), [2,2,3,4,5,5,5,5])

    def test_empty_input(self):
        self.assertEqual(cut([], 1, 3), [])

    def test_exception(self):
        with self.assertRaises(ValueError):
            cut([1,2,3], 4, 3)
            
if __name__ == '__main__':
    unittest.main()