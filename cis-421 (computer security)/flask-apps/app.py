from flask import Flask, request, render_template
from cipher.cesar_cipher import caesar_cipher
from cipher.simple_substitution_cipher import encrypt as sub_encrypt, decrypt as sub_decrypt, generate_cipher_mapping
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        operation = request.form['operation']
        result_text = caesar_cipher(text, shift)
        return render_template('index.html', result_text=result_text, text=text, shift=shift, operation=operation)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)