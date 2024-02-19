# problems-2/assignment-1
def pythagorean_threes(n):
    return [(x, y, z) for x in range(n)
            for y in range(n)
            for z in range(n)
            if x ** 2 + y ** 2 == z ** 2]


print(pythagorean_threes(6))

