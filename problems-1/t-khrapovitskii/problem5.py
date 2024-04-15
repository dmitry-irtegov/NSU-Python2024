import pytest


def get_primes(limit: int) -> list[int]:
    is_prime = [False, False] + [True] * (limit - 1)
    for i in range(2, limit + 1):
        if is_prime[i]:
            for j in range(i * 2, limit + 1, i):
                is_prime[j] = False
    return [i for i, x in enumerate(is_prime) if x]


def factorize(number: int) -> list[tuple[int, int]]:
    if number < 2:
        raise ValueError(f"Cannot factorize number {number}")
    primes = get_primes(number)
    ret = []
    for prime in primes:
        times = 0
        while number % prime == 0:
            times += 1
            number //= prime
        if times:
            ret.append((prime, times))
    return ret


class Test:
    def test_get_primes_small(self):
        assert get_primes(0) == []
        assert get_primes(1) == []
        assert get_primes(2) == [2]
        assert get_primes(3) == [2, 3]
        assert get_primes(4) == [2, 3]

    def test_get_primes(self):
        assert get_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_factorize_edge_case(self):
        with pytest.raises(ValueError):
            factorize(-10)
        with pytest.raises(ValueError):
            factorize(0)
        with pytest.raises(ValueError):
            factorize(1)

    def test_factorize_small(self):
        assert factorize(2) == [(2, 1)]
        assert factorize(3) == [(3, 1)]
        assert factorize(4) == [(2, 2)]
        assert factorize(5) == [(5, 1)]
        assert factorize(6) == [(2, 1), (3, 1)]

    def test_factorize(self):
        assert factorize(360) == [(2, 3), (3, 2), (5, 1)]
