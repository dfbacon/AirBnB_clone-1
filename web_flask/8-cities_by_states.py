#!/usr/bin/python3
'''
This is the '8-cities_by_state' module.

8-citites_by_state utilizes Flask to start a web application:
* listening on 0.0.0.0
* port 5000
* Integrage with sqlalchemy
'''
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def state_list():
    states = storage.all("State")
    return (render_template("8-cities_by_states.html", states=states))


@app.teardown_appcontext
def close_out(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
