import sys

def cumulative_sum(seq):
    result = [0 for i in range(0, len(seq) + 1)]
    for i in range(0, len(seq) + 1):
        result[i] = sum(seq[0:i])
    return result

def simple_tests():
    assert cumulative_sum([0, 0, 0]) == [0, 0, 0, 0]
    print(cumulative_sum([0, 0, 0]))

    assert cumulative_sum([1, 2, 3]) == [0, 1, 3, 6]
    print(cumulative_sum([1, 2, 3]))

    assert cumulative_sum([1, 1, 1]) == [0, 1, 2, 3]
    print(cumulative_sum([1, 1, 1]))

    assert cumulative_sum([0.5, -0.36, 3.1456]) == [0, 0.5, 0.14, 3.2856]
    print(cumulative_sum([0.5, -0.36, 3.1456]))

    assert cumulative_sum([-1, -2, -3]) == [0, -1, -3, -6]
    print(cumulative_sum([-1, -2, -3]))

    assert cumulative_sum([sys.maxsize, 2, 3]) == [0, sys.maxsize, sys.maxsize + 2, sys.maxsize + 2 + 3]
    print(cumulative_sum([sys.maxsize, 2, 3]))

    print('All tests passed.')

simple_tests()