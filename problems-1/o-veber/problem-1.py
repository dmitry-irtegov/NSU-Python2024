def cusum(input_array):
    res = [0] + [None] * len(input_array)
    for i in range(len(input_array)):
        res[i + 1] = input_array[i] + res[i]
    return res


assert cusum([]) == [0]
assert cusum([0, 0, 0]) == [0, 0, 0, 0]
assert cusum([0, 1, 2, 3, 10]) == [0, 0, 1, 3, 6, 16]