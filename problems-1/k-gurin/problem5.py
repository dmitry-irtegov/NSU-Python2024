# problems-1/assignment-5
import unittest


def prime_factors(n):
    result = []
    probe = 2
    i = temp = count = 0
    while n != 1:
        if n % probe != 0:
            probe += 1
        else:
            n /= probe
            if temp != probe:
                result.append([probe])
                if count != 0:
                    result[i - 1].append(count)
                i += 1
                count = 0
            count += 1
            temp = probe
    result[i - 1].append(count)
    return result


class PrimeFactors(unittest.TestCase):
    def test_init(self):
        self.assertEqual([[2, 2], [3, 1]], prime_factors(12))

    def test_prime(self):
        self.assertEqual([[3571, 1]], prime_factors(3571))

    def test_big_split_number(self):
        self.assertEqual([[2, 1], [3, 2], [11, 1], [17, 1], [37, 1]], prime_factors(124542))


if __name__ == '__main__':
    unittest.main()
