#!/usr/bin/python3
from models import *
from sqlalchemy import Table, Column, Integer, String, DateTime
import os


class Amenity(BaseModel, Base):
    '''This is the 'Amenity' class'''
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
