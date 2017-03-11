#!/usr/bin/python3
from models import *
from sqlalchemy import Table, Column, Integer, String, DateTime
import os

class State(BaseModel):
    '''This is the 'State' class'''
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
