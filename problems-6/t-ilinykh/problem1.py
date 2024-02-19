import random

def shuffle_letters(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def sort_letters(word):
    letters = list(word)
    letters.sort()
    return ''.join(letters)

def transform_text(text, transformation):
    transformed_words = [transformation(word) for word in text.split()]
    return ' '.join(transformed_words)

def main():
    text = input("Введите текст: ")
    random_result = transform_text(text, shuffle_letters)
    sorted_result = transform_text(text, sort_letters)

    print("Исходный текст:")
    print(text)
    print("Случайная перестановка букв:")
    print(random_result)
    print("Сортировка букв по алфавиту:")
    print(sorted_result)

if __name__ == "__main__":
    main()
