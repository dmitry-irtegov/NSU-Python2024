from math import sqrt


def primes(n: int) -> list[int]:
    return [
        cand for cand in range(2, n + 1)
        if all(cand % check for check in range(2, int(sqrt(cand)) + 1))
    ]
