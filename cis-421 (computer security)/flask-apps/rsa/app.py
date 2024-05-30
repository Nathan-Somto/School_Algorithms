from flask import Flask, request, render_template
from rsa_python import rsa_encrypt, rsa_decrypt, rsa_key_pair
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def rsa():
    if request.method == 'POST':
        if 'generate_keys' in request.form:
            public_key, private_key = rsa_key_pair()
            return render_template('rsa.html', public_key=public_key, private_key=private_key)
        
        text = request.form['text']
        public_key = tuple(map(int, request.form['public_key'].strip('()').split(',')))
        private_key = tuple(map(int, request.form['private_key'].strip('()').split(',')))
        operation = request.form['operation']

        if operation == 'encrypt':
            result_text = rsa_encrypt(text, public_key)
        else:
            result_text = rsa_decrypt(eval(text), private_key)
            return render_template('rsa.html', result_text=result_text, text=text, public_key=public_key, private_key=private_key, operation=operation)

    return render_template('rsa.html')
if __name__ == '__main__':
    app.run(debug=True)