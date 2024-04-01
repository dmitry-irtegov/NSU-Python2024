import problem5
import problem5_Eratosthenes
import unittest
import time


class PerformanceCompetition(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(problem5_Eratosthenes.sieve_of_eratosthenes(0), [])
        self.assertEqual(problem5.prime_divisors(0), [])
        self.assertEqual(problem5_Eratosthenes.sieve_of_eratosthenes(1), [])
        self.assertEqual(problem5.prime_divisors(1), [])
        self.assertEqual(problem5_Eratosthenes.sieve_of_eratosthenes(-123), [[3, 1], [41, 1]])
        self.assertEqual(problem5.prime_divisors(-123), [[3, 1], [41, 1]])
        self.assertEqual(problem5_Eratosthenes.sieve_of_eratosthenes(123), [[3, 1], [41, 1]])
        self.assertEqual(problem5.prime_divisors(123), [[3, 1], [41, 1]])
        self.assertEqual(problem5_Eratosthenes.sieve_of_eratosthenes(562), [[2, 1], [281, 1]])
        self.assertEqual(problem5.prime_divisors(562), [[2, 1], [281, 1]])
        self.assertEqual(problem5_Eratosthenes.sieve_of_eratosthenes(12), [[2, 2], [3, 1]])
        self.assertEqual(problem5.prime_divisors(12), [[2, 2], [3, 1]])

    def test_small_value(self):
        start_time = time.time()
        res_simple = problem5.prime_divisors(53134932)
        print(f"Simple algorithm time: {time.time() - start_time}")
        start_time = time.time()
        res_erato = problem5_Eratosthenes.sieve_of_eratosthenes(53134932)
        print(f"Eratosthenes sieve time: {time.time() - start_time}")
        self.assertEqual(res_simple, res_erato)

    def test_medium_value(self):
        start_time = time.time()
        res_simple = problem5.prime_divisors(53134343932)
        print(f"Simple algorithm time: {time.time() - start_time}")
        start_time = time.time()
        res_erato = problem5_Eratosthenes.sieve_of_eratosthenes(53134343932)
        print(f"Eratosthenes sieve time: {time.time() - start_time}")
        self.assertEqual(res_simple, res_erato)

    def test_large_value(self):
        start_time = time.time()
        res_simple = problem5.prime_divisors(421542465436754)
        print(f"Simple algorithm time: {time.time() - start_time}")
        start_time = time.time()
        res_erato = problem5_Eratosthenes.sieve_of_eratosthenes(421542465436754)
        print(f"Eratosthenes sieve time: {time.time() - start_time}")
        self.assertEqual(res_simple, res_erato)

    def test_simple_value(self):
        start_time = time.time()
        res_simple = problem5.prime_divisors(454547865385769)
        print(f"Simple algorithm time: {time.time() - start_time}")
        start_time = time.time()
        res_erato = problem5_Eratosthenes.sieve_of_eratosthenes(454547865385769)
        print(f"Eratosthenes sieve time: {time.time() - start_time}")
        self.assertEqual(res_simple, res_erato)


if __name__ == '__main__':
    unittest.main()
