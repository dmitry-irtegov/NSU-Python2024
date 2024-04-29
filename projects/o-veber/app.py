from flask import Flask, render_template, request
from spellchecker import SpellChecker
from CaesarCipherProvider import CaesarCipherProvider

app = Flask(__name__)
cipher_provider = CaesarCipherProvider()


def decode_caesar_with_spellcheck(ciphertext, language_name='en'):
    spellchecker = SpellChecker(language=language_name)
    best_shift = 0
    min_mistakes = float('inf')

    language = cipher_provider.find_language(language_name)
    for shift in range(language.get_alphabet_power()):
        decrypted_text = cipher_provider.decode(ciphertext, shift, language)
        mistakes = sum([1 for word in decrypted_text.split() if word.lower() not in spellchecker])

        if mistakes < min_mistakes:
            min_mistakes = mistakes
            best_shift = shift

    return cipher_provider.decode(ciphertext, best_shift, language), language.get_alphabet_power() - best_shift


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        encrypted_text = request.form['text']
        language = request.form.get('language', 'en')
        decrypted_text, shift = decode_caesar_with_spellcheck(encrypted_text, language)
        return render_template('index.html', decrypted_text=decrypted_text, shift=shift, original_text=encrypted_text)
    return render_template('index.html', decrypted_text='', shift='', original_text='')


if __name__ == '__main__':
    app.run(debug=True)
