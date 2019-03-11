# noinspection PyUnresolvedReferences
import rsa, elgamal, dh, re_encryption

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/ajax/<name>', methods=('POST', ))
def ajax(name):
    result = eval('{}.{}()'.format(name, request.form['method']))
    return jsonify(result)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/page/<name>')
def page(name):
    return render_template('{}.html'.format(name))


if __name__ == '__main__':
    app.run(debug=True)
