#!/usr/bin/python3
'''
This is the '7-states_list' module.

7-states_list utilizes Flask to start a web application:
* listening on 0.0.0.0
* port 5000
* Integrage with sqlalchemy
'''
from models import storage
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

app = Flask(__name__)


@app.route('/states_list/')
def list_states():
    """list all states in a db"""
    states = storage.all("State").values()
    return render_template("7-states_list.html",
                           Query_name="States", states=states)


@app.teardown_appcontext
def close_session(exception):
    """remove the session to see what happened"""
    storage.close()


if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")
