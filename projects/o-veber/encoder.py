import argparse

from CaesarCipherProvider import CaesarCipherProvider, ShiftType

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='Текст для кодирования')
    parser.add_argument('shift', type=int, help='Величина сдвига букв')
    parser.add_argument('--lang', type=str, default='ru', choices=['ru', 'en'],
                        help='Язык текста (русский по умолчанию)')
    args = parser.parse_args()

    cipher_provider = CaesarCipherProvider()
    encoded_text = cipher_provider.get_text_with_shift_for_language_name(args.text, args.shift, args.lang,
                                                                         ShiftType.ENCODE)
    print("Закодированный текст:", encoded_text)
