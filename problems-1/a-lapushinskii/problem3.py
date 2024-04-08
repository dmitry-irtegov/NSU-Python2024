import unittest

def collatz_row(n):
    yield n
    while n > 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        yield n

def print_row_string(generator):
    for i in generator:
        if (i <= 1):
            print(1)
            break
        print(str(i), end = " -> ")
    

###
    
class TestCollatzRow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(list(collatz_row(3)), [3, 10, 5, 16, 8, 4, 2, 1])
    def test(self):
        self.assertEqual(list(collatz_row(4)), [4, 2, 1])
    def test_minus(self):
        self.assertEqual(list(collatz_row(-1)), [-1])
    def test_gen(self):
        gen = collatz_row(4)
        self.assertEqual(next(gen), 4)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 1)
        try :
            next(gen)
            self.assertEqual(1, 2)
        except Exception:
            return

if __name__ == '__main__':
    unittest.main()
