#!/usr/bin/python3
'''
This is the '6-number_odd_or_even' module.

6-number_odd_or_even utilizes Flask to start a web application:
* listening on 0.0.0.0
* port 5000
* (/) displays "Hello HBNB!"
* (/hbnb) displays "HBNB"
* (/c/<text>) displays "c text"
* (/python/<text>) displays "python text"; text default = 'is cool'
* (/number/<n>) display "n" only if n is integer
* (/number_template/<n>) display HTML page only if n is integer
* (/number_odd_or_even/<n>) display HTML page only if n is integer
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb')
def hello_hbnb():
    return ('HBNB')


@app.route('/c/<text>')
def hello_c(text):
    txt = text.replace('_', ' ')
    return ('c {}'.format(txt))


@app.route('/python/')
@app.route('/python')
@app.route('/python/<text>')
def hello_python(text="is cool"):
    txt = text.replace('_', ' ')
    return ('Python {}'.format(txt))


@app.route('/number/<int:n>')
def hello_number(n):
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>')
def number_even_odd(n):
    text = "is odd"
    if n % 2 == 0:
        text = "is even"
    return (render_template('6-number_odd_or_even.html', n=n, text=text))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
