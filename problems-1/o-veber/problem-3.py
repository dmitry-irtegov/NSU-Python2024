def check_collatz_hypothesis(number):
    history = [str(number)]
    while number != 1:
        number = number // 2 if (number % 2 == 0) else (3 * number + 1)
        history.append(str(number))
    return history


if __name__ == '__main__':
    print("Write digit")
    digit = int(input())
    print(' → '.join(check_collatz_hypothesis(digit)))
