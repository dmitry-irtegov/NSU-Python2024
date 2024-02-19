from collections.abc import Iterable
from typing import TypeVar

N = TypeVar("N", int, float, int | float)

def cumulative_sums(nums: Iterable[N]) -> list[N]:
    current: N = 0
    return [(current := current + n) for n in nums]
