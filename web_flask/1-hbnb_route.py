#!/usr/bin/python3

""" 1-hbnb_route module """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
