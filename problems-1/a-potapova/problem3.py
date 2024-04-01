def do_step(number: int) -> int:
    return number // 2 if number % 2 == 0 else 3 * number + 1


def collatz_hypothesis(number: int):
    result = []
    current_number = number
    while current_number != 1:
        current_number = do_step(current_number)
        result.append(current_number)
    return result


if '__main__' == __name__:
    input_number = int(input("Введите число: "))
    sequence = collatz_hypothesis(input_number)
    print(input_number, end="")
    for num in sequence:
        print(f" -> {num}", end="")
