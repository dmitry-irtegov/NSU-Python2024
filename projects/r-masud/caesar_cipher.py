from spellchecker import SpellChecker
from string import ascii_lowercase as en_lower, ascii_uppercase as en_upper

class Language:
    def __init__(self, name, alphabets, alphabet_size):
        self.name = name
        self.alphabets = alphabets
        self.alphabet_size = alphabet_size

    def get_name(self):
        return self.name

    def get_alphabets(self):
        return self.alphabets

    def get_alphabet_size(self):
        return self.alphabet_size

class CaesarCipher:
    def __init__(self):
        ru_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.languages = [
            Language('ru', [ru_lower, ru_upper], 33),
            Language('en', [en_lower, en_upper], 26)
        ]

    def get_language(self, name):
        for language in self.languages:
            if language.get_name() == name:
                return language
        raise ValueError(f"Language {name} not supported")

    def identify_language(self, text):
        char_count = {lang.get_name(): 0 for lang in self.languages}
        for language in self.languages:
            for alphabet in language.get_alphabets():
                char_count[language.get_name()] += sum(1 for char in text if char in alphabet)
        detected_language = max(char_count, key=char_count.get)
        return self.get_language(detected_language)

    def shift_character(self, char, shift, language, mode):
        alphabets = language.get_alphabets()
        for alphabet in alphabets:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index + shift) % language.get_alphabet_size() if mode == 'ENCODE' else (index - shift) % language.get_alphabet_size()
                return alphabet[new_index]
        return char

    def apply_shift(self, text, shift, language, mode):
        if language.get_name() == 'en':
            if mode == 'DECODE':
                return decrypt_english(text, shift)
            else:
                return ''.join(self.shift_character(char, shift, language, mode) for char in text)
        elif language.get_name() == 'ru':
            if mode == 'DECODE':
                return decrypt_russian(text, shift)
            else:
                return encrypt_russian(text, shift)
        return text

    def auto_decrypt(self, text, language):
        spell = SpellChecker(language=language.get_name())
        max_correct_words = 0
        best_shift = 0
        best_text = text

        for shift in range(language.get_alphabet_size()):
            decrypted_text = self.apply_shift(text, shift, language, 'DECODE')
            words = decrypted_text.split()
            correct_words = sum(1 for word in words if spell.correction(word) == word)
            if correct_words > max_correct_words:
                max_correct_words = correct_words
                best_shift = shift
                best_text = decrypted_text

        return best_text, best_shift

def decrypt_english(msg, shift):
    decrypted_text = ""
    for char in msg:
        if char.isalpha():
            base_ord = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - base_ord - shift) % 26 + base_ord)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_russian(msg, shift):
    llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    ulst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    encrypted_text = ""
    for char in msg:
        if char.lower() in llst:
            ind = llst.index(char.lower()) + shift
            encrypted_char = ulst[ind % len(llst)] if char.islower() else ulst[ind % len(llst)].lower()
            encrypted_text += encrypted_char
        elif char in ulst:
            ind = ulst.index(char) + shift
            encrypted_text += ulst[ind % len(ulst)]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_russian(msg, shift):
    llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    ulst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    decrypted_text = ""
    for char in msg:
        if char.lower() in llst:
            ind = llst.index(char.lower())
            decrypted_ind = (ind - shift) % len(llst)
            decrypted_char = llst[decrypted_ind].upper() if char.isupper() else llst[decrypted_ind]
            decrypted_text += decrypted_char
        elif char in ulst:
            ind = ulst.index(char)
            decrypted_ind = (ind - shift) % len(ulst)
            decrypted_char = ulst[decrypted_ind].lower() if char.islower() else ulst[decrypted_ind]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def resolve_ambiguities(decrypted_text, language):
    spell = SpellChecker(language=language)
    corrected_text = []
    for word in decrypted_text.split():
        corrected_word = spell.correction(word)
        if corrected_word is not None:
            corrected_text.append(corrected_word)
        else:
            corrected_text.append(word)  # Keep the original word if it couldn't be corrected
    return ' '.join(corrected_text)

