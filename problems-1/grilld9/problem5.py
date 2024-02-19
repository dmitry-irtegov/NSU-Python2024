import math

def prime_divisors(num):
    result = []
    idx = 0
    divisor = 2
    while num != 1:
        if is_simple(divisor):
            if num % divisor == 0:
                degree = 1
                result.append([divisor, degree])
                num //= divisor
                while num % divisor == 0:
                    degree += 1
                    result[idx][1] = degree
                    num //= divisor
                idx += 1
        divisor += 1
    return result
def is_simple(num):
    sqrt_rounded = round(math.sqrt(num))
    for i in range(2, sqrt_rounded + 1):
        if num % i == 0:
            return False
    return True

print("Ex5 output: ", prime_divisors(123))
