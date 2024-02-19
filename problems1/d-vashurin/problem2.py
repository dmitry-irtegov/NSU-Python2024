from collections.abc import MutableSequence
from typing import TypeVar

N = TypeVar("N", int, float, int | float)

def bound_seq(nums: MutableSequence[N], lower: N, upper: N) -> None:
    if lower > upper:
        message = f"{lower = } is greater than {upper =}"
        raise ValueError(message)

    for index, num in enumerate(nums):
        if num < lower:
            nums[index] = num
        elif upper < num:
            nums[index] = upper
