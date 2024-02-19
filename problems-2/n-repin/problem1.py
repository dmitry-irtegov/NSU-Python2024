def pythagorean_triples(n: int) -> list[tuple[int, int, int]]:
    return [ (a, b, c) for a in range(1, n) for b in range(1, n) for c in range(1, n) if a*a + b*b == c*c ]


if __name__ == "__main__":
    print(pythagorean_triples(20))