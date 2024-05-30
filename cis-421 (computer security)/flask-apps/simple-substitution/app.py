from flask import Flask, request, render_template
from simple_substitution_python import generate_cipher_mapping, decrypt, encrypt
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def subsitution():
    if request.method == 'POST':
        text = request.form['text']
        operation = request.form['operation']
        result_text = ''
        cipher_mapping = generate_cipher_mapping()
        if operation == 'encrypt':
            result_text = encrypt(text, cipher_mapping)
        else:
            result_text = decrypt(text, cipher_mapping)
        return render_template('index.html', result_text=result_text, text=text, operation=operation)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)