def cumulative_sums(nums):
    sum = 0
    result = [0] * (len(nums) + 1)
    result[0] = sum
    for idx, num in enumerate(nums):
        sum += num
        result[idx + 1] = sum
    return result


ex_input = [1, 2, 3]
print("Ex1 output:", cumulative_sums(ex_input))
