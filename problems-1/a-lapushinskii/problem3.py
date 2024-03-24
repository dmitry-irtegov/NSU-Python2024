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
    row = list(generator)
    for i in row[:-1]:
        print(str(i), end = " -> ")
    if row:
        print(row[-1])
    
n = int(input())
print_row_string(collatz_row(n))

###
    
class TestCollatzRow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(list(collatz_row(3)), [3, 10, 5, 16, 8, 4, 2, 1])
    def test(self):
        self.assertEqual(list(collatz_row(4)), [4, 2, 1])
    def test_minus(self):
        self.assertEqual(list(collatz_row(-1)), [-1])

if __name__ == '__main__':
    unittest.main()
