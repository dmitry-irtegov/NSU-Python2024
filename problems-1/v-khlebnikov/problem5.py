def get_primes(x):
    primes = [i for i in range(x + 1)]
    primes[1] = 0
    for i in range(2, x + 1):
        if primes[i] != 0:
            j = 2 * i
            while j <= x:
                primes[j] = 0
                j = j + i
    return [i for i in primes if i != 0]


def factorize(x, use_primes=True):
    multipliers = []
    for i in (get_primes(x) if use_primes else range(2, x + 1)):
        if x == 1:
            break
        m = [i, 0]
        while x % i == 0:
            m[1] += 1
            x /= i
        if m[1] != 0:
            multipliers.append(m)
    return multipliers


print(factorize(123123, use_primes=False))
