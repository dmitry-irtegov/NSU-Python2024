def get_collatz_list(n):
    res = [n]
    while True:
        if(n%2 == 0):
            n = n // 2
        else:
            n = 3*n + 1

        res.append(n)
        if n == 1:
            break

    return res

def print_arrows(arr):
    for x in arr[:-1]:
        print(x, end=" -> ")
    print(arr[-1])

def print_collatz(n):
    print_arrows(get_collatz_list(n))

if __name__ == '__main__':
    n = int(input())
    print_arrows(get_collatz_list(n))