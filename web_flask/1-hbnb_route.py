#/usr/bin/python3
'''
This is the '1-hbnb_route' module.

1-hbnb_route utilizes Flask to start a web application:
* listening on 0.0.0.0,
* port 5000,
* (/) displays "Hello HBNB!"
* (/hbnb) displays "HBNB"
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb')
def hello_hbnb():
    return ('HBNB')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
