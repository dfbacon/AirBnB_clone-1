#!/usr/bin/python3
'''
This is the '8-cities_by_state' module.

8-citites_by_state utilizes Flask to start a web application:
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


def cities_by_statess():
    """List all cities by states"""
    states = storage.all("State").values()
    cities = storage.all("City").values()
    result = [[state, [city for city in cities if city.state_id == state.id]]
              for state in states]
    result.sort(key=lambda x: x[0].name)
    return(render_template("8-cities_by_states.html",
                           Query_name="States", result=result))


@app.route('/cities_by_states/')
def cities_by_states():
    """List all cities by states"""
    states = storage.all("State").values()
    result = []
    for state in sorted(states, key=lambda x: x.name):
        result.append([state, state.cities])
    return(render_template("8-cities_by_states.html",
                           Query_name="States", result=result))


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session or save file"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
