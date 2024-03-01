def pythagorean_triples(n: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, c)
        for c in range(1, n + 1)
        for b in range(1, c + 1)
        for a in range(1, b + 1)
        if a * a + b * b == c * c
    ]
