from typing import Collection, Iterable, Self
from sieve import Sieve

from bitarray import bitarray


class BitArraySieve(Sieve):
    def __init__(self, n: int):
        self.n = n
        self.sieve = bitarray(n + 1)
        self.sieve[0] = True
        self.sieve[1] = True

    @classmethod
    def create(cls, n: int) -> Self:
        return cls(n)

    def set_composites(self, composites: Iterable[int]):
        for composite in composites:
            self.sieve[composite] = True

    def is_known_composite(self, number: int) -> bool:
        return self.sieve[number] == 1

    def get_primes(self) -> Collection[int]:
        return tuple(i for i in range(2, self.n + 1) if self.sieve[i] == 0)
