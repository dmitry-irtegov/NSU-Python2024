import unittest
from Buckets import Buckets
from FixedBuckets import FixedBuckets

class TestBuckets(unittest.TestCase):
  
    def test_change_default(self):
        def_list = [1, 2, 3]
        buc = Buckets(1, def_list)
        def_list.append(4)
        self.assertEqual(buc.buckets[0], [1, 2, 3, 4])
        
    def test_common_default(self):
        def_list = [1, 2, 3]
        buc = Buckets(2, def_list)
        buc.add(0, 4)
        self.assertEqual(buc.buckets[1], [1, 2, 3, 4])
    
    def test_common_state(self):
        buc = Buckets(2, [1, 2, 3])
        buc.add(0, 4)
        self.assertEqual(buc.buckets[0], buc.buckets[1])
        
    def test_common_clear(self):
        buc = Buckets(2, [])
        buc.buckets[0] = [1, 2]
        buc.buckets[1] = [3, 4]
        buc.clear(0)
        buc.clear(1)
        buc.add(0, 4)
        self.assertEqual(buc.buckets[0], buc.buckets[1])
        
    def test_bad_length(self):
        buc = Buckets(-1, [1, 2, 3])
        with self.assertRaises(IndexError):
            buc.add(0, 4)
        
    def test_bad_type(self):
        buc = Buckets(2, "hello world")
        with self.assertRaises(AttributeError):
            buc.add(0, 4)
            
class TestFixedBuckets(unittest.TestCase):
  
    def test_change_default(self):
        def_list = [1, 2, 3]
        buc = FixedBuckets(1, def_list)
        def_list.append(4)
        self.assertNotEqual(buc.buckets[0], [1, 2, 3, 4])
        
    def test_common_default(self):
        def_list = [1, 2, 3]
        buc = FixedBuckets(2, def_list)
        buc.add(0, 4)
        self.assertNotEqual(buc.buckets[1], [1, 2, 3, 4])
    
    def test_common_state(self):
        buc = FixedBuckets(2, [1, 2, 3])
        buc.add(0, 4)
        self.assertNotEqual(buc.buckets[0], buc.buckets[1])
        
    def test_common_clear(self):
        buc = FixedBuckets(2, [])
        buc.buckets[0] = [1, 2]
        buc.buckets[1] = [3, 4]
        buc.clear(0)
        buc.clear(1)
        buc.add(0, 4)
        self.assertNotEqual(buc.buckets[0], buc.buckets[1])
        
    def test_bad_length(self):
        with self.assertRaises(ValueError):
            FixedBuckets(-1, [1, 2, 3])
        
    def test_bad_type(self):
        with self.assertRaises(TypeError):
            FixedBuckets(2, 666)
  
if __name__ == "__main__":
  unittest.main()