#!/usr/bin/python3
'''
This is the '10-hbnb_filters' module.

10-hbnb_filters utilizes Flask to start a web application:
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
import sys

app = Flask(__name__)


@app.route('/states/')
def show_states():
    states = storage.all("State").values()
    return(render_template('9-states.html', states=states, selected="Only"))


@app.route('/states/<id_name>')
def show_cities(id_name):
    states = storage.all("State").values()
    for item in states:
        if str(item.id) == id_name:
            state = item
            return(render_template('9-states.html', states=state,
                                   state="State"))
    state = 'None'
    return(render_template('9-states.html', states=state, state="None"))



@app.route('/hbnb_filters')
def display_filters():
    """ display html page with filters """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return(render_template('10-hbnb_filters.html', states=states,
                           amenity=amenities))


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session or save file"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
