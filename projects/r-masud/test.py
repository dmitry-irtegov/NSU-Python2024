from spellchecker import SpellChecker

def caesar_encrypt(text, shift, language):
    if language == 'en':
        return encrypt_english(text, shift)
    elif language == 'ru':
        return encrypt_russian(text, shift)
    else:
        return "Unsupported language"

def caesar_decrypt(text, shift, language):
    if language == 'en':
        return decrypt_english(text, shift)
    elif language == 'ru':
        return decrypt_russian(text, shift)
    else:
        return "Unsupported language"

def encrypt_english(msg, shift):
    encrypted_text = ""
    for char in msg:
        if char.isalpha():
            base_ord = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - base_ord + shift) % 26 + base_ord)
        else:
            encrypted_text += char
    return encrypted_text

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
    llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
            'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
            'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    encrypted_text = ""
    for char in msg:
        if char in llst:
            ind = llst.index(char) % len(llst)
            encrypted_text += llst[(ind + shift) % len(llst)]
        elif char in blst:
            ind = blst.index(char) % len(llst)
            encrypted_text += blst[(ind + shift) % len(llst)]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_russian(msg, shift):
    llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
            'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    decrypted_text = ""
    for char in msg:
        if char.lower() in llst:
            ind = llst.index(char.lower())
            decrypted_ind = (ind - shift) % len(llst)
            decrypted_char = llst[decrypted_ind].upper() if char.isupper() else llst[decrypted_ind]
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

def main():
    original_text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value for encryption: "))
    language = input("Enter 'en' for English or 'ru' for Russian: ")

    encrypted_text = caesar_encrypt(original_text, shift, language)
    print("Encrypted text:", encrypted_text)

    decrypted_text = caesar_decrypt(encrypted_text, shift, language)
    resolved_text = resolve_ambiguities(decrypted_text, language)
    print("Decrypted and resolved text:", resolved_text)

if __name__ == "__main__":
    main()
