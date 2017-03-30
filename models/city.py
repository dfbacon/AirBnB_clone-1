#!/usr/bin/python3
'''
This is the 'city' module.
'''
from models.base_model import BaseModel, Base, Table, Column, String
from sqlalchemy import ForeignKey
from os import getenv


class City(BaseModel, Base):
    '''This is the 'City' class'''
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization method'''
        super().__init__(*args, **kwargs)
