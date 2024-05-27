from bitarray import bitarray
import time
import unittest

def eratosthenes_list(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return primes

def eratosthenes_set(n):
    sieve = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in sieve:
            sieve.difference_update(range(i*i, n+1, i))  
    return sieve

def eratosthenes_bitarray(n):
    sieve = bitarray(n + 1)
    sieve.setall(True)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [p for p in range(n + 1) if sieve[p]]

class EratosthenTests(unittest.TestCase):
    def test_unit_list(self):
        primes_list = eratosthenes_list(10)
        self.assertEqual(primes_list, [2,3,5,7])

    def test_unit_set(self):
        primes_set = eratosthenes_set(10)
        self.assertEqual(primes_set, {2,3,5,7})

    def test_unit_bits(self):
        primes_bits = eratosthenes_bitarray(10)
        self.assertEqual(primes_bits, [2,3,5,7])

    def test_n_list(self):
        start_time = time.time()
        primes_list = eratosthenes_list(100000000)
        end_time = time.time()
        self.assertEqual(primes_list[499], 3571)
        print("list -", round(end_time - start_time, 2), "секунд")

    def test_n_set(self):
        start_time = time.time()
        primes_set = eratosthenes_set(100000000)
        end_time = time.time()
        self.assertTrue(3547 in primes_set)
        print("set -", round(end_time - start_time,2), "секунд")

    def test_n_bits(self):
        start_time = time.time()
        primes_bits = eratosthenes_bitarray(100000000)
        end_time = time.time()
        self.assertEqual(primes_bits[497], 3557)
        print("bitarray -", round(end_time - start_time,2), "секунд")

if __name__ == '__main__':
    unittest.main()
