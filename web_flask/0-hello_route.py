#!/usr/bin/python3
'''
This is the '0-hello_route' module.

0-hello_route utilizes Flask to start a web application:
* listening on 0.0.0.0,
* port 5000,
* displays "Hello HBNB!"
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hello HBNB!')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
