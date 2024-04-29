import argparse

from CaesarCipherProvider import CaesarCipherProvider

def caesar_decipher(text, shift, lang):
    """
    Функция декодирует текст, закодированный с помощью шифра Цезаря.

    :param text: текст для декодирования
    :param shift: величина сдвига букв (целое число)
    :param lang: язык текста (ru или en)
    :return: декодированный текст
    """

    language = cipher_provider.find_language(lang)

    decoded = [None] * len(text)
    for i, letter in enumerate(text):
        if letter in language.get_alphabet():
            index = language.get_alphabet().index(letter)
            new_index = (index - shift) % language.get_alphabet_power()
            decoded[i] = language.get_alphabet()[new_index]
        else:
            decoded[i] = letter

    return ''.join(decoded)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='Текст для декодирования')
    parser.add_argument('shift', type=int, help='Величина сдвига букв')
    parser.add_argument('--lang', type=str, default='ru', choices=['ru', 'en'],
                        help='Язык текста (русский по умолчанию)')
    args = parser.parse_args()

    cipher_provider = CaesarCipherProvider()
    decoded_text = caesar_decipher(args.text, args.shift, args.lang)
    print("Декодированный текст:", decoded_text)
