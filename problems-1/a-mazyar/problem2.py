import unittest

def prune_array(array, a, b):
    for i, x in enumerate(array):
        if x < a:
            array[i]= a
        elif x > b:
            array[i] = b
    return array

class TestPruneArray(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(prune_array([0,1,2,3,4,5], 2, 3), [2,2,2,3,3,3])

    def test_negatives(self):
        self.assertEqual(prune_array([-5,-4,-3,-2,-1,0], -3, -2), [-3,-3,-3,-2,-2,-2])

    def test_same_bounds(self):
        self.assertEqual(prune_array([0,1,2,3,4,5], 0, 0), [0]*6)

    def test_empty_array(self):
        self.assertEqual(prune_array([], -1, 1), [])

    def test_floats(self):
        self.assertEqual(prune_array([0.3,1.3,2.3,3.3,4.3,5.3], 2.1, 3.4), [2.1,2.1,2.3,3.3,3.4,3.4])
        

if __name__ == "__main__":
    unittest.main()