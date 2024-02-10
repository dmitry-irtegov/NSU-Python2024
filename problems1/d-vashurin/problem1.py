from collections.abc import Iterable


def cumulative_sums(nums: Iterable[int | float | complex]) -> list[int | float | complex]:
    current: int | float | complex = 0
    return [(current := current + n) for n in nums]
