import argparse


def translate(input_string, translate_from, translate_to, delete):
    if len(translate_from) != len(translate_to):
        raise ValueError("Количество символов в строках замены не совпадает ")
    translate_table = {}
    result = list(input_string)
    for idx, char in enumerate(translate_from):
        translate_table[char] = translate_to[idx]
    for char in delete:
        translate_table[char] = ''
    for idx, char in enumerate(input_string):
        if char in translate_table:
            result[idx] = translate_table[char]
    return ''.join(result)


def main():
    parser = argparse.ArgumentParser(description='Изменяет заданные символы файла на другие символы')
    parser.add_argument('string', type=str)
    parser.add_argument('translate_from', type=str)
    parser.add_argument('translate_to', type=str)
    parser.add_argument('-d', '--delete', type=str)
    args = parser.parse_args()
    translate(args.string, args.translate_from, args.translate_to, args.delete)


if __name__ == '__main__':
    main()
