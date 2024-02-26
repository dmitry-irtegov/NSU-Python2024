
# modifies input array
def bound(array, lower_bound, upper_bound):
    for i in range(len(array)):
        array[i] = array[i] if array[i] > lower_bound else lower_bound
        array[i] = array[i] if array[i] < upper_bound else upper_bound
    return array
