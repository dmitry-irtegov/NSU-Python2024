def factorize_number(num):
    if num == 1:
        return [1, 1]
    elif num < 1:
        raise Exception("Number must be positive")

    prime = 2
    factor_list = []

    while prime * prime <= num:
        power_list = [prime, 0]
        while num % prime == 0:
            power_list[1] += 1
            num //= prime
        if power_list[1] > 0:
            factor_list.append(power_list)
        prime += 1

    if num > 1:
        factor_list.append([num, 1])

    return factor_list


if __name__ == "__main__":
    number = int(input())
    print(factorize_number(number))
