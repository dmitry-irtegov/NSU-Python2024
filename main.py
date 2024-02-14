# problems-1/assignment-3
def collatz_hypothesis():
    n = int(input())
    trans_chain = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        trans_chain.append(n)
    return trans_chain


print(collatz_hypothesis())

