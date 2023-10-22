#!/usr/bin/python3

""" 2-c_route module """

from flask import Flask, abort, render_template
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


@app.route('/number/<n>', strict_slashes=False)
def show_isnumber(n):
    """ Displaying number if integer """
    if n.isdigit():
        return '{} is a number'.format(n)
    abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def show_number_template(n):
    """ Display a HTML page only if n is an integer """
    if n.isdigit():
        return render_template('5-number.html', n=n)
    abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def show_odd_even(n):
    """ Display a HTML page only if n is an integer
        and shows if n is odd or even
    """
    if n.isdigit():
        return render_template('6-number_odd_or_even.html', n=int(n))
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
