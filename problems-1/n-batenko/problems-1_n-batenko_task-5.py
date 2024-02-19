from math import sqrt

def get_primes_powers_naive(n):
    
    num = n

    def is_prime(num, primes):
        for i in range(2, int(sqrt(num)) + 1, 2):
            if num in primes:
                return True
            else:
                if num % i == 0:
                    return False
        return True
    
    result = []
    primes = []
    if not is_prime(num, primes):
        k = 1
        for factor in range(2, num // 2 + 1, k):  #make it correct
            if (not is_prime(factor, primes)):
                continue
            power = 0
            while num % factor == 0:
                num //= factor
                power += 1
            if (power == 0):
                continue
            else:
                primes.append(factor)
                result.append((factor, power))

            if factor == 3: k += 1
    else:
        result.append((num, 1))

    return result

print(get_primes_powers_naive(1235788))