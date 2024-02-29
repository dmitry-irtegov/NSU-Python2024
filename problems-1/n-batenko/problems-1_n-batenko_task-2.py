import unittest

def substitution_function(seq, a, b):
    result = [0 for i in range(len(seq))]
    if a > b:
        raise Exception('Lower bound is higher than Higher bound.')
    for i in range(len(seq)):
        num = seq[i]
        temp = num
        if num < a:
            temp = a
        elif num > b:
            temp = b
        result[i] = temp
    return result

class SubstiotutionTests(unittest.TestCase):
    def test_equals_dif(self):
        print(substitution_function([0, 0, 0], 1, 5))
        self.assertEqual(substitution_function([0, 0, 0], 1, 5), [1, 1, 1])
    
    def test_dif_equals(self):
        print(substitution_function([-100, 10, 100], -99, 99))
        self.assertEqual(substitution_function([-100, 10, 100], -99, 99), [-99, 10, 99])

    def test_equals_equals(self):
        print(substitution_function([0, 0, 0], 0, 0))
        self.assertEqual(substitution_function([0, 0, 0], 0, 0), [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
