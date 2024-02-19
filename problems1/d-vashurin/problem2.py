from collections.abc import MutableSequence


def bound_seq(nums: MutableSequence[int | float], lower: int | float, upper: int | float) -> None:
    if lower > upper:
        message = f"{lower = } is greater than {upper =}"
        raise ValueError(message)

    for index, num in enumerate(nums):
        if num < lower:
            nums[index] = num
        elif upper < num:
            nums[index] = upper
