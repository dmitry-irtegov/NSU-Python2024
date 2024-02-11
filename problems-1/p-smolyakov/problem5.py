def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True

def primes_list(n):
    return [x for x in range(2, n+1) if is_prime(x)]

import unittest
class PrimesListTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        size = 200000
        self.__primes_list = primes_list(size)

    def test_zero(self):
        self.assertFalse(0 in self.__primes_list)

    def test_one(self):
        self.assertFalse(1 in self.__primes_list)

    def test_two(self):
        self.assertTrue(2 in self.__primes_list)

    def test_fourtynine(self):
        self.assertFalse(49 in self.__primes_list)

    def test_largeprime(self):
        self.assertTrue(199999 in self.__primes_list)

    def test_largenonprime(self):
        self.assertFalse(199997 in self.__primes_list)

if __name__ == '__main__':
    unittest.main()
