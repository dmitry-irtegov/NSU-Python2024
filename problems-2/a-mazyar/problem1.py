import unittest
from timeit import Timer

def pythag_triples(n):
    return [(x,y,z) for x in range(1,n+1)
            for y in range(1,n+1)
            for z in range(1,n+1)
            if x**2 + y**2 == z**2]

def unique_pythag_triples(n):
    return [(x,y,z) for x in range(1,n+1)
            for y in range(x,n+1) # we begin with x because triplet where y is smaller is just permutation
            for z in range(y,n+1) # z is obviously bigger than y
            if x**2 + y**2 == z**2]

class TestPythagTriplets(unittest.TestCase):
    def test_by_size(self):
        self.assertEqual(len(unique_pythag_triples(5)), 1)
        self.assertEqual(len(unique_pythag_triples(25)), 8)
        self.assertEqual(len(unique_pythag_triples(50)), 20)

if __name__ == '__main__':
    t = Timer(lambda: pythag_triples(200))
    print(t.timeit(number=1))

    t = Timer(lambda: unique_pythag_triples(200))
    print(t.timeit(number=1))

    unittest.main()