def pythagorean_triples(limits):
    c, m = 0, 2
    triples = []

    while c < limits:

        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > limits:
                break

            triples.append((a, b, c))

        m = m + 1
    return triples


if __name__ == "__main__":
    length = int(input())
    print(pythagorean_triples(length))
