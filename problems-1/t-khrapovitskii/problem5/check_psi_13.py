import random

from problem5 import is_prime

strong_pseudoprimes = [318665857834031151167461,
                       2995741773170734841812261,
                       667636712015520329618581,
                       3317044064679887385961981,
                       3317044064679887385961981,
                       552727880697763694556181,
                       360681321802296925566181,
                       7395010240794120709381,
                       3404730287403079539471001,
                       164280218643672633986221]


class TestPsi13:
    def test_psi_11(self):
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for i in strong_pseudoprimes:
            assert is_prime(i, a)

    def test_psi_12(self):
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

        works = [318665857834031151167461,
                 667636712015520329618581,
                 552727880697763694556181]

        for i in works:
            assert is_prime(i, a)

    def test_psi_13(self):
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        works = [318665857834031151167461,
                 2995741773170734841812261,
                 667636712015520329618581,
                 552727880697763694556181,
                 360681321802296925566181,
                 7395010240794120709381,
                 3404730287403079539471001,
                 164280218643672633986221]
        for i in works:
            assert not is_prime(i, a)

    def test_psi_14(self):
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43]
        for i in strong_pseudoprimes:
            assert not is_prime(i, a)


def check_random_n(x, n):
    a = [random.randint(2, x - 2) for _ in range(n)]
    return not is_prime(x, a)


if __name__ == '__main__':
    passed = 0
    total = 0
    try:
        for _ in range(10000000):
            x = random.choice(strong_pseudoprimes)
            if check_random_n(x, 9):
                passed += 1
            total += 1
    except KeyboardInterrupt:
        pass
    finally:
        print(f"Passed {passed} out of {total}")
