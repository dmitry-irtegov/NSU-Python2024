# problems-1/assignment-2
def cut_numbers(arr, a, b):
    for i in range(len(arr)):
        if arr[i] < a:
            arr[i] = a
        if arr[i] > b:
            arr[i] = b
    return arr


print(cut_numbers([1, 2, 3, 13, 20, 30, 50, 60, 70], 12, 34))

