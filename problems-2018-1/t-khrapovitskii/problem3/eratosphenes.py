from sieve import Sieve


def eratosthenes(sieve: Sieve, n: int):
    for i in range(2, n + 1):
        if not sieve.is_known_composite(i):
            sieve.set_composites(range(i * 2, n + 1, i))
