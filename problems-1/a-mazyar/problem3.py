def check_collatz(n):
    print(n, end="")
    if(n == 1):
        print()
        return
    print(" -> ", end="")
    if(n%2 == 0):
        check_collatz(n//2)
    else:
        check_collatz(3*n + 1)

check_collatz(3)
check_collatz(5)
check_collatz(10)
check_collatz(15)