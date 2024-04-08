def caesar_decrypt(text, shift, language):
    if language == 'en':
        return decrypt_english(text, shift)
    elif language == 'ru':
        return decrypt_russian(text, shift)
    else:
        raise ValueError("Unsupported language")


def decrypt_english(msg, shift):
    decrypted_text = ""
    for char in msg:
        if char.isalpha():
            base_ord = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - base_ord - shift) % 26 + base_ord)
        else:
            decrypted_text += char
    return decrypted_text


def decrypt_russian(msg, shift):
    lowercase_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    uppercase_alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    decrypted_text = ""
    for char in msg:
        if char.lower() in lowercase_alphabet:
            ind = lowercase_alphabet.index(char.lower())
            decrypted_ind = (ind - shift) % len(lowercase_alphabet)
            decrypted_char = uppercase_alphabet[decrypted_ind] if char.isupper() else lowercase_alphabet[decrypted_ind]
            decrypted_text += decrypted_char
        elif char in uppercase_alphabet:
            ind = uppercase_alphabet.index(char)
            decrypted_ind = (ind - shift) % len(uppercase_alphabet)
            decrypted_char = uppercase_alphabet[decrypted_ind].lower() if char.islower() else uppercase_alphabet[decrypted_ind]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


import unittest

class TestCaesarDecrypt(unittest.TestCase):

    def test_decrypt_english(self):
        # Test decryption with English language
        encrypted_text = "Wklv lv d whvw phvvdjh."
        expected_decrypted_text = "This is a test message."
        decrypted_text = caesar_decrypt(encrypted_text, 3, 'en')
        self.assertEqual(decrypted_text, expected_decrypted_text)

    def test_decrypt_russian(self):
        # Test decryption with Russian language
        encrypted_text = "ящръ жйж лг ящръ амр а хгк амномп"
        expected_decrypted_text = "быть или не быть вот в чем вопрос"
        decrypted_text = caesar_decrypt(encrypted_text, 31, 'ru')
        self.assertEqual(decrypted_text, expected_decrypted_text)

    def test_unsupported_language(self):
        # Test unsupported language
        encrypted_text = "Wklv lv d whvw phvvdjh."
        with self.assertRaises(ValueError):
            caesar_decrypt(encrypted_text, 3, 'fr')


if __name__ == '__main__':
    unittest.main()