import unittest

import buckets.buckets as b
import buckets.buckets_fix as bf



class TestBuckets(unittest.TestCase):
    def test_adds_to_one(self):
        buck = b.Buckets(2, [])
        buck.add(0, 1)
        self.assertTrue(buck.find(0, 1))
        self.assertFalse(buck.find(1, 1))

    def test_default_persists(self):
        test_default = []
        buck = b.Buckets(2, test_default)
        test_default.append(1)
        self.assertFalse(buck.find(0, 1))
    
    def test_clears_only_one(self):
        buck = b.Buckets(2, [])
        buck.add(0, 1)
        buck.add(1, 1)
        buck.clear(0)

        self.assertFalse(buck.find(0, 1))
        self.assertTrue(buck.find(1, 1))

class TestBucketsFix(unittest.TestCase):
    def test_adds_to_one(self):
        buck = bf.Buckets(2, [])
        buck.add(0, 1)
        self.assertTrue(buck.find(0, 1))
        self.assertFalse(buck.find(1, 1))

    def test_default_persists(self):
        test_default = []
        buck = bf.Buckets(2, test_default)
        test_default.append(1)
        self.assertFalse(buck.find(0, 1))
        
    def test_clears_only_one(self):
        buck = bf.Buckets(2, [])
        buck.add(0, 1)
        buck.add(1, 1)
        buck.clear(0)
        
        self.assertFalse(buck.find(0, 1))
        self.assertTrue(buck.find(1, 1))

if __name__ == "__main__":
    unittest.main()