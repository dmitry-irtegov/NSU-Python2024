def trim_list(data, lower_bound, upper_bound):
    def trim_fn(elem, lb, ub):
        return lb if elem < lb else ub

    return [trim_fn(elem, lower_bound, upper_bound) for elem in data]


if __name__ == "__main__":
    data = list(map(int, input().split()))
    lower_bound, upper_bound = map(int, input().split())
    print(trim_list(data, lower_bound, upper_bound))
