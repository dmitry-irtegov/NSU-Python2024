# problems-1/assignment-1
#! /usr/bin/python
def cumulative_sum(arr):
    ans = [0] * (len(arr) + 1)
    for i, v in enumerate(arr, start=1):
        ans[i] = ans[i-1] + v
    return ans