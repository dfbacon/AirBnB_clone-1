#!/usr/bin/python3
'''
This is the 'amenity' module.
'''
from models import *
from sqlalchemy import Table, Column, Integer, String, DateTime


class Amenity(BaseModel, Base):
    '''This is the 'Amenity' class'''
    if Base is not object:
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization method'''
        super().__init__(*args, **kwargs)
