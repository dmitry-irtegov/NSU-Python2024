from functools import reduce


def cumulative_sum(data):
    if not data:
        raise Exception("Number sequence is empty")
    else:
        return f"Your list: {reduce(lambda acc, x: [*acc, acc[-1] + x], data, [0])}"


if __name__ == "__main__":
    my_list = list(map(int, input().split()))
    print(cumulative_sum(my_list))
