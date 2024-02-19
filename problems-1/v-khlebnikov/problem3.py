def collatz_hypothesis(x):
    print(x, end=" ")
    while x > 1:
        print("->", end=" ")
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        print(x, end=" ")


if __name__ == '__main__':
    x = input()
    collatz_hypothesis(int(x))
