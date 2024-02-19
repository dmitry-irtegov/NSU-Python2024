def seq_cut(nums, a, b):
    for idx, num in enumerate(nums):
        if num < a:
            nums[idx] = a
        elif num > b:
            nums[idx] = b
    return nums

ex_input = [1, 2, 3]
print("Ex2 output:", seq_cut(ex_input, 2, 2))
