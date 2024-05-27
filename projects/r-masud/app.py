from flask import Flask, render_template, request
from caesar_cipher import CaesarCipher, resolve_ambiguities


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def decrypt_text():
    if request.method == 'POST':
        encrypted_text = request.form.get('encrypted_text', '')

        if encrypted_text:
            cipher = CaesarCipher()
            language_obj = cipher.identify_language(encrypted_text)
            language = language_obj.get_name()
            decrypted_text, best_shift = cipher.auto_decrypt(encrypted_text, language_obj)
            resolved_text = resolve_ambiguities(decrypted_text, language)
            return render_template('result.html',
                                   encrypted_text=encrypted_text,
                                   shift=best_shift,
                                   language=language,
                                   decrypted_text=decrypted_text,
                                   resolved_text=resolved_text)
        else:
            error_message = "Please enter encrypted text."
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
