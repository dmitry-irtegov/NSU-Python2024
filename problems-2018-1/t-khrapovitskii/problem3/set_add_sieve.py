from typing import Collection, Iterable, Self

from sieve import Sieve


class SetAddSieve(Sieve):
    def __init__(self, n: int):
        self.n = n
        self.sieve: set[int] = set()

    @classmethod
    def create(cls, n: int) -> Self:
        return cls(n)

    def set_composites(self, composites: Iterable[int]):
        for composite in composites:
            self.sieve.add(composite)

    def is_known_composite(self, number: int) -> bool:
        return number in self.sieve

    def get_primes(self) -> Collection[int]:
        return tuple(i for i in range(2, self.n + 1) if i not in self.sieve)
