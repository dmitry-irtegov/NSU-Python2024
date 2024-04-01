import math


def sieve_of_eratosthenes(num):
    result = []
    if num == 0:
        return result
    elif num < 0:
        num = abs(num)
    sieve_size = round(math.sqrt(num)) + 1
    sieve = [0] * sieve_size
    for divisor in range(2, sieve_size):
        if num == 1:
            return result
        if sieve[divisor] == 0:
            if num % divisor == 0:
                degree = 0
                while num % divisor == 0:
                    num //= divisor
                    degree += 1
                result.append([divisor, degree])
            for i in range(divisor, sieve_size, divisor):
                sieve[i] = 1
    if num != 1:
        result.append([num, 1])
    return result


if '__main__' == __name__:
    print(sieve_of_eratosthenes(int(input())))
