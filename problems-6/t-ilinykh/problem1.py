# -*- coding: utf-8 -*-

import random
import sys

def shuffle_letters(word):
    if len(word) <= 3:
        return word
    first_letter, *middle_letters, last_letter = word
    random.shuffle(middle_letters)
    return first_letter + ''.join(middle_letters) + last_letter

def sort_letters(word):
    if len(word) <= 3:
        return word
    return word[0] + ''.join(sorted(word[1:-1])) + word[-1]

def transform_text(text, transformation):
    words = []
    current_word = []
    for char in text:
        if char.isalnum():
            current_word.append(char)
        else:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
            words.append(char)
    if current_word:
        words.append(''.join(current_word))
    transformed_words = [transformation(word) if word.isalpha() else word for word in words]
    return ''.join(transformed_words)

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
