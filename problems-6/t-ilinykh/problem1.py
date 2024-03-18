# coding= utf-8

import random
import sys

def shuffle_letters(word):
    letters = list(word)
    if len(letters) <= 3:
        return word
    first_letter, *middle_letters, last_letter = letters
    random.shuffle(middle_letters)
    return ''.join([first_letter] + middle_letters + [last_letter])

def sort_letters(word):
    letters = list(word)
    letters.sort()
    return ''.join(letters)

def transform_text(text, transformation):
    transformed_words = [transformation(word) for word in text.split()]
    return ' '.join(transformed_words)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    text = input("Введите текст: ")
    try:
        random_result = transform_text(text, shuffle_letters)
        sorted_result = transform_text(text, sort_letters)
        print("Исходный текст:")
        print(text)
        print("Случайная перестановка букв:")
        print(random_result)
        print("Сортировка букв по алфавиту:")
        print(sorted_result)
    except TypeError as e:
        print("Ошибка типа данных при обработке текста:", e)
    except ValueError as e:
        print("Ошибка значения при обработке текста:", e)

if __name__ == "__main__":
    main()
