from typing import Generator


def cumulative_sum_list(numbers: list[int]) -> list[int]:
    sums = [ 0 ] * (len(numbers) + 1)

    for (i, number) in enumerate(numbers):
        sums[i + 1] = sums[i] + number

    return sums


def cumulative_sum_generator(numbers: list[int]) -> Generator[int, list[int], None]:
    yield 0

    csum = 0

    for number in numbers:
        csum += number

        yield csum


if __name__ == "__main__":
    print([ x for x in cumulative_sum_generator([1, 2, 3]) ])
    print([ x for x in cumulative_sum_generator([]) ])
    print([ x for x in cumulative_sum_generator([15]) ])
    print([ x for x in cumulative_sum_generator([1, 2, 3, 4]) ])

    print()

    print(cumulative_sum_list([1, 2, 3]))
    print(cumulative_sum_list([]))
    print(cumulative_sum_list([15]))
    print(cumulative_sum_list([1, 2, 3, 4]))