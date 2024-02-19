
def substitution_function(seq, a, b):
    result = []
    if a > b:
        raise Exception('Lower bound is higher than Higher bound.')
    for num in seq:
        temp = num
        if num < a:
            temp = a
        elif num > b:
            temp = b
        result.append(temp)
    return result

def simple_tests():
    assert substitution_function([0, 0, 0], 1, 5) == [1, 1, 1]
    assert substitution_function([-100, 10, 100], -99, 99) == [-99, 10, 99]
    assert substitution_function([0, 0, 0], 0, 0) == [0, 0, 0]

    print('All tests passed.')

simple_tests()
