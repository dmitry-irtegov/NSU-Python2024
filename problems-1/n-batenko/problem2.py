import unittest

def substitution_function(seq, a, b):
    if a > b:
        raise Exception('Exception: Lower bound is higher than upper bound.')
    
    result = [0] * (len(seq))

    for i in range(len(seq)):
        num = seq[i]
        temp = num
        if num < a:
            temp = a
        elif num > b:
            temp = b
        result[i] = temp
    return result

class SubstitutionTests(unittest.TestCase):
    def test_equals_dif(self):
        print(substitution_function([0, 0, 0], 1, 5))
        self.assertEqual(substitution_function([0, 0, 0], 1, 5), [1, 1, 1])
    
    def test_dif_equals(self):
        print(substitution_function([-100, 10, 100], -99, 99))
        self.assertEqual(substitution_function([-100, 10, 100], -99, 99), [-99, 10, 99])

    def test_equals_equals(self):
        print(substitution_function([0, 0, 0], 0, 0))
        self.assertEqual(substitution_function([0, 0, 0], 0, 0), [0, 0, 0])
    
    def test_exception(self):
        with self.assertRaises(Exception) as context:
            substitution_function([0, 0, 0], 5, 1)
        
        self.assertTrue('Exception: Lower bound is higher than upper bound.' in str(context.exception))
        
if __name__ == '__main__':
    unittest.main()


