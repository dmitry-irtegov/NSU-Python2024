from functools import reduce

def primes_factorization(num):
    ans = []
    i = 2
    while num > 1:
        power = 0

        while num % i == 0:
            num //= i
            power += 1

        if power > 0:
            ans.append((i, power))
        i += 1

    return ans

if __name__ == '__main__':
    print('type an integer number to factorize:')
    num = int(input())
    ans = primes_factorization(num)

    # print(ans)
    print(reduce(lambda a, b: f'{a} * {b}', map(lambda pair: f'{pair[0]}^{pair[1]}', ans)), f'= {num}')
