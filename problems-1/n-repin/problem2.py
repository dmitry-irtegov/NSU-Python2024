def limit(numbers: list[int], lower: int, upper: int) -> list[int]:
    return [ num if lower < num < upper else (lower if num <= lower else upper) for num in numbers ]

if __name__ == "__main__":
    print(limit([x for x in range(10)], 3, 6))