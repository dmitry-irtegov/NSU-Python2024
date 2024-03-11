import unittest


def primes_list(n):
    return [x for x in range(2, n + 1) if not any(x % divider == 0 for divider in range(2, x // 2 + 1))]


class PrimesListTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        size = 20000
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
        self.assertTrue(19997 in self.__primes_list)

    def test_largenonprime(self):
        self.assertFalse(19971 in self.__primes_list)
        self.assertFalse(20000 in self.__primes_list)

if __name__ == '__main__':
    unittest.main()
