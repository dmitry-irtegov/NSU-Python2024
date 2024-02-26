import unittest

def collatz_row(n):
    row = [n]
    while (n > 1):
        if(n%2 == 1):
            n = 3*n + 1
            row.append(n)
        n = n//2
        row.append(n)
    return row

def get_row_string(row):
    ans = str(row.pop(0))
    for i in row:
        ans += " -> " + str(i)
    return ans

n = int(input())
print(get_row_string(collatz_row(n)))

###
    
class TestCollatzRow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(collatz_row(3), [3, 10, 5, 16, 8, 4, 2, 1])
    def test(self):
        self.assertEqual(collatz_row(4), [4, 2, 1])
    def test_minus(self):
        self.assertEqual(collatz_row(-1), [-1])

if __name__ == '__main__':
    unittest.main()
