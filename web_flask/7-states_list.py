#!/usr/bin/python3
'''
This is the '7-states_list' module.

7-states_list utilizes Flask to start a web application:
* listening on 0.0.0.0
* port 5000
* Integrage with sqlalchemy
'''
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states_list')
def state_list():
    states = storage.all("State")
    return (render_template("7-states_list.html", states=states))


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
