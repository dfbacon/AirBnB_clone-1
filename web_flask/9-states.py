#!/usr/bin/python3
'''
This is the '9-states' module.

9-states utilizes Flask to start a web application:
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


@app.route('/states/')
@app.route('/states/<id_name>')
def cities_by_states(id_name="all"):
    states = storage.all("State")
    if id_name == "all":
        return(render_template("9-states.html", state="all",
                               Query_name="States", states=states.values()))
    else:
        flag = False
        for key, value in states.items():
            if key == id_name:
                flag = True
                break
        if flag:
            result = value.cities
            return(render_template("9-states.html", state="1",
                                   Query_name="State: {}".format(value.name),
                                   states=result))
        else:
            return(render_template("9-states.html", state="",
                                   Query_name="Not found",
                                   states=states))


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session or save file"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
