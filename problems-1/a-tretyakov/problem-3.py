def collatz_hypothesis(num, chain=None):
    if chain is None:
        chain = [num]

    if num == 0:
        return "Number doesn't satisfies Collatz hypothesis"
    if num == 1:
        return f"Transformation chain of the Collatz hypothesis: {chain}"

    num = num // 2 if num % 2 == 0 else num * 3 + 1
    return collatz_hypothesis(num, [*chain, num])


if __name__ == "__main__":
    number = int(input())
    print(collatz_hypothesis(number))
