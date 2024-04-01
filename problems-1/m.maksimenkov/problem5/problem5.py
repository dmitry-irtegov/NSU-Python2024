import math


def prime_divisors(num):
    result = []
    if num == 0:
        return result
    elif num < 0:
        num = abs(num)
    for divisor in range(2, round(math.sqrt(num)) + 1):
        if num == 1:
            return result
        degree = 0
        if num % divisor == 0:
            while num % divisor == 0:
                num //= divisor
                degree += 1
            result.append([divisor, degree])
    if num != 1:
        result.append([num, 1])
    return result


if '__main__' == __name__:
    print(prime_divisors(int(input())))
