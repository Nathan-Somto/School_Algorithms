from vignere_otp_cipher_python import vignere_otp_cipher
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def otp_cipher():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        operation = request.form['operation']
        to_encrypt = operation == 'encrypt'
        result_text = vignere_otp_cipher(text, key, to_encrypt)
        return render_template('index.html', result_text=result_text, text=text, key=key, operation=operation)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)