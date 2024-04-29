import argparse

from CaesarCipherProvider import CaesarCipherProvider


def caesar_cipher(text, shift, lang):
    """
    Функция кодирует текст с помощью шифра Цезаря.

    :param text: текст для кодирования
    :param shift: величина сдвига букв (целое число)
    :param lang: язык текста (ru или en)
    :return: закодированный текст
    """

    language = cipher_provider.find_language(lang)

    encoded = [None] * len(text)
    for i, letter in enumerate(text):
        if letter in language.get_alphabet():
            index = language.get_alphabet().index(letter)
            new_index = (index + shift) % language.get_alphabet_power()
            encoded[i] = language.get_alphabet()[new_index]
        else:
            encoded[i] = letter

    return ''.join(encoded)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='Текст для кодирования')
    parser.add_argument('shift', type=int, help='Величина сдвига букв')
    parser.add_argument('--lang', type=str, default='ru', choices=['ru', 'en'],
                        help='Язык текста (русский по умолчанию)')
    args = parser.parse_args()

    cipher_provider = CaesarCipherProvider()
    encoded_text = caesar_cipher(args.text, args.shift, args.lang)
    print("Закодированный текст:", encoded_text)
