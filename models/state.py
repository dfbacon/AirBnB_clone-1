#!/usr/bin/python3
'''
This is the 'state' module.
'''
from models import *
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''This is the 'State' class'''
    if Base is not object:
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""
        cities = [""]

    def __init__(self, *args, **kwargs):
        '''This is the initialization method'''
        super(State, self).__init__(*args, **kwargs)
