def cumulative_sums(nums):
    sum = 0
    result = [sum]
    for num in nums:
        sum += num
        result.append(sum)
    return result

ex_input = [1, 2, 3]
print("Ex1 output:", cumulative_sums(ex_input))