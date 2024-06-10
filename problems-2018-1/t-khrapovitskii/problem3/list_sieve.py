from typing import Collection, Iterable, Self

from sieve import Sieve


class ListSieve(Sieve):
    def __init__(self, n: int):
        self.n = n
        self.sieve = [True] * (n + 1)
        self.sieve[0] = False
        self.sieve[1] = False

    @classmethod
    def create(cls, n: int) -> Self:
        return cls(n)

    def set_composites(self, composites: Iterable[int]):
        for composite in composites:
            self.sieve[composite] = False

    def is_known_composite(self, number: int) -> bool:
        return not self.sieve[number]

    def get_primes(self) -> Collection[int]:
        return tuple(i for i in range(2, self.n + 1) if self.sieve[i])
