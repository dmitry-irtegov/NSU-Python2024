import unittest

def cumulative(a):
    res = [0]*(len(a) + 1)
    sum = 0
    for i in a:
        sum += i
        res.append(sum)
    return res

class TestFirstTask(unittest.TestCase):
    def test_example(self):
        self.assertEqual(cumulative([1,2,3]),[0,1,3,6])

    def test_null(self):
        self.assertEqual(cumulative([]),[0])

    def test_big(self):
        self.assertEqual(cumulative([1,3,5,7,9,3,1,4,6,9,0,0,0,7,4,2]),[0,1,4,9,16,25,28,29,33,39,48,48,48,48,55,59,61])

if __name__ == '__main__':
    unittest.main()
