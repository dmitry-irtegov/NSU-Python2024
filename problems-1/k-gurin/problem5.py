# problems-1/assignment-5
def prime_factors(n):
    result = []
    probe = 2
    i = temp = count = 0
    while n != 1:
        if n % probe != 0:
            probe += 1
        else:
            n /= probe
            if temp != probe:
                result.append([probe])
                if count != 0:
                    result[i-1].append(count)
                i += 1
                count = 0
            count += 1
            temp = probe
    result[i - 1].append(count)
    return result


print(prime_factors(12))

