import unittest
import sys

def collatz(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n

class TestCollatz(unittest.TestCase):

    def test_collatz_1(self):
        self.assertEqual(list(collatz(1)), [1])

    def test_collatz_2(self):
        self.assertEqual(list(collatz(2)), [2, 1])

    def test_collatz_3(self):
        self.assertEqual(list(collatz(3)), [3, 10, 5, 16, 8, 4, 2, 1])

def main():
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            sys.stderr.write("Number must be positive.\n")
        else:
            print("Sequence of transformations:")
            for seq in collatz(num):
                print(seq, end=' ')
                if seq != 1:
                    print("->", end=' ')
            print()
    except ValueError:
        sys.stderr.write("Error: please enter an integer.\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        unittest.main(argv=sys.argv[:1]) 
    else:
        main()
