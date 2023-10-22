#!/usr/bin/python3

""" 2-c_route module """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displaying a welcoming hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    """ Displaying just a hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_foo(text):
    """ Displaying C followed by an entered text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def show_python_foo(text='is cool'):
    """ Displaying Python followed by an entered text """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(debug=True)
