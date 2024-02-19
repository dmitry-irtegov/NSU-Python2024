
inputString = input()
numbers_list = [int(x) for x in inputString.split()]


def cum_sum(numbers):
    res = [0] * (len(numbers_list) + 1)
    for i, number in enumerate(numbers, 1):
        res[i] = number + res[i - 1]
    return res


print(cum_sum(numbers_list))
