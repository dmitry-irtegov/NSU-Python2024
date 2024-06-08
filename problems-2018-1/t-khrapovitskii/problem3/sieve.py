from abc import ABC, abstractmethod
from collections.abc import Iterable, Collection
from typing import Self


class Sieve(ABC):
    @classmethod
    @abstractmethod
    def create(cls, n: int) -> Self:
        ...

    @abstractmethod
    def set_composites(self, composites: Iterable[int]):
        # composites must be between 2 and N
        ...

    @abstractmethod
    def is_known_composite(self, number: int) -> bool:
        # number must be between 2 and N
        ...

    @abstractmethod
    def get_primes(self) -> Collection[int]:
        ...
