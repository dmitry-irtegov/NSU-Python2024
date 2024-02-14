# problems-1/assignment-1
def cumulative_sum(arr):
    s = 0
    ans = [s]
    for i in range(len(arr)):
        s += arr[i]
        ans.append(s)
    return ans


print(cumulative_sum([1, 2, 3]))

