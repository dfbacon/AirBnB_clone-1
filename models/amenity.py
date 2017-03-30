#!/usr/bin/python3
'''
This is the 'amenity' module.
'''
from models.base_model import BaseModel, Base, Table, Column, String
from os import getenv


class Amenity(BaseModel, Base):
    '''This is the 'Amenity' class'''
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization method.
        '''
        super().__init__(*args, **kwargs)
