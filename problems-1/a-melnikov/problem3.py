def collatz_hypothesis(n: int) -> list[int]:
    trace: list[int] = [n]
    while (num := trace[-1]) != 1:
        if num % 2 == 0:
            trace.append(num // 2)
        else:
            trace.append(3 * num + 1)
    return trace

if __name__ == "__main__":
    x = int(input())
    trace = collatz_hypothesis(x)
    print(" -> ".join(map(str, trace)))
