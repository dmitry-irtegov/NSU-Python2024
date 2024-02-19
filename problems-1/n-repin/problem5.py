from math import ceil, sqrt


def first_divisor(num: int) -> int | None:
    bound = ceil(sqrt(num))

    for i in range(2, bound + 1):
        if num % i == 0:
            return i

    return None


def insert_or_inc(map: dict[int, int], key: int):
        if key in map:
            map[key] += 1
        else:
            map[key] = 1


def primes(number: int) -> list[tuple[int, int]]:
    prime_map = {}
    
    while (divisor := first_divisor(number)) is not None:
        insert_or_inc(prime_map, divisor)

        number //= divisor

    insert_or_inc(prime_map, number)

    return [ (p, k) for (p, k) in prime_map.items() if p != 1 ]


def format_primes_list(map: list[tuple[int, int]]) -> str:
    terms = []

    for item in map:
        (p, k) = item
        terms.append(f"{p}^{k}")

    return " * ".join(terms)


if __name__ == "__main__":
    for i in range(2, 100):
        print(i, format_primes_list(primes(i)))
