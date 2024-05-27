from problem5 import is_prime

N_IN_FILE = 1000000
FILES = ['./check_is_prime/primes1.txt', './check_is_prime/primes50.txt']

good = 0
total_numbers = 0


def assert_prime(n):
    global good
    if not is_prime(n, 1):
        print(n, "is prime, identified as composite")
    else:
        good += 1


def assert_comp_between(start, end):
    global good
    for n in range(start + 1, end):
        if is_prime(n, 1):
            print(n, "is composite, identified as prime")
        else:
            good += 1


if __name__ == '__main__':
    for filename in FILES:
        with open(filename, 'r') as f:
            for i in range(4):
                f.readline()
            nums = map(int, f.read().split())
            # nums_l = list(nums)
            cur_prime = next(nums)
            assert_prime(cur_prime)
            total_numbers -= cur_prime - 1
            for i, x in enumerate(nums):
                prev_prime = cur_prime
                cur_prime = x
                assert_prime(cur_prime)
                assert_comp_between(prev_prime, cur_prime)
                if (i + 1) % (N_IN_FILE // 20) == 0:
                    print(filename, i + 1)
            total_numbers += cur_prime
        print()
    print(f"Good: {good} out of {total_numbers}")
