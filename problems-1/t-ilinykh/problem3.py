def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    try:
        num = int(input("Введите число: "))
        if num <= 0:
            print("Число должно быть положительным.")
            return
        sequence = collatz(num)
        print("Цепочка преобразований:")
        for seq in sequence:
            print(seq, end = ' ')
            if seq != sequence[len(sequence)-1]:
                print("->", end = ' ')
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()
