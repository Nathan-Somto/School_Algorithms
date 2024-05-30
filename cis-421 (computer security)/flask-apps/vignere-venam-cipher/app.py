from flask import Flask, request, render_template
from vignere_venam_cipher_python import vignere_venam_cipher

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        operation = request.form['operation']
        to_encrypt = operation == 'encrypt'
        result_text = vignere_venam_cipher(text, key, to_encrypt)
        return render_template('index.html', result_text=result_text, text=text, key=key, operation=operation)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
