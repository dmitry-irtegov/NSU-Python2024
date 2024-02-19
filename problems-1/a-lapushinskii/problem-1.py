
def sum_cumulative (arr):
    result = [0] * (len(arr)+1)
    for i, x in enumerate(arr):
        result[i+1] = result[i] + x
    return result

print(sum_cumulative([1, 2, 3]))
