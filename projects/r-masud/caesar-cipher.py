
from flask import Flask, render_template, request
from spellchecker import SpellChecker


def caesar_decrypt(text, shift, language):
    if language == 'en':
        return decrypt_english(text, shift)
    elif language == 'ru':
        return decrypt_russian(text, shift)
    else:
        return "Unsupported language"



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
    llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё']
    ulst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'Ё']
    decrypted_text = ""
    for char in msg:
        if char.lower() in llst:
            ind = llst.index(char.lower())
            decrypted_ind = (ind - shift) % len(llst)
            decrypted_char = ulst[decrypted_ind] if char.isupper() else llst[decrypted_ind]
            decrypted_text += decrypted_char
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


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def decrypt_text():
    if request.method == 'POST':
        encrypted_text = request.form.get('encrypted_text', '')  # Retrieve encrypted text from form
        shift = int(request.form.get('shift', '3'))  # Retrieve shift value from form (default to 3)
        language = request.form.get('language', 'en')  # Retrieve language selection from form (default to English)

        if encrypted_text:
            decrypted_text = caesar_decrypt(encrypted_text, shift, language)
            resolved_text = resolve_ambiguities(decrypted_text, language)
            return render_template('result.html',
                                   encrypted_text=encrypted_text,
                                   shift=shift,
                                   language=language,
                                   decrypted_text=decrypted_text,
                                   resolved_text=resolved_text)  # Pass decrypted and resolved texts separately
        else:
            error_message = "Please enter encrypted text."
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)