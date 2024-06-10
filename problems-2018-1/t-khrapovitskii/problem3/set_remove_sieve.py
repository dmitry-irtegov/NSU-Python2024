from typing import Collection, Iterable, Self

from sieve import Sieve


class SetRemoveSieve(Sieve):
    def __init__(self, n: int):
        self.n = n
        self.sieve = set(range(2, n + 1))

    @classmethod
    def create(cls, n: int) -> Self:
        return cls(n)

    def set_composites(self, composites: Iterable[int]):
        for composite in composites:
            self.sieve.discard(composite)

    def is_known_composite(self, number: int) -> bool:
        return number not in self.sieve

    def get_primes(self) -> Collection[int]:
        return set(self.sieve)
