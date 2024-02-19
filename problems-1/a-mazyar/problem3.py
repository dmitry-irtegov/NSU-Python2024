import unittest

def get_collatz_list(n):
    res = [n]
    while True:
        if n <= 1:
            break
        if(n%2 == 0):
            n = n // 2
        else:
            n = 3*n + 1

        res.append(n)

    return res

def print_arrows(arr):
    for x in arr[:-1]:
        print(x, end=" -> ")
    print(arr[-1])

def print_collatz(n):
    print_arrows(get_collatz_list(n))

class TestCollatzCheck(unittest.TestCase):
    def test_simple_examples(self):
        self.assertEqual(get_collatz_list(5), [5,16,8,4,2,1])
        self.assertEqual(get_collatz_list(0), [0])

if __name__ == '__main__':
    n = int(input())
    print_arrows(get_collatz_list(n))
    unittest.main()