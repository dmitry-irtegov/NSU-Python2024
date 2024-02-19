from math import ceil, sqrt


def get_primes_to_powers(digit):
    resulted_list = []
    for i in range(2, ceil(sqrt(digit)) + 1):
        result = 0
        while digit != 1 and digit % i == 0:
            digit /= i
            result += 1
        if result > 0:
            resulted_list.append((i, result))
    return resulted_list


assert get_primes_to_powers(12) == [(2, 2), (3, 1)]
assert get_primes_to_powers(0) == []
assert get_primes_to_powers(1) == []
assert get_primes_to_powers(2) == [(2, 1)]
