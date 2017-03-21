#!/usr/bin/python3
from models import *
from sqlalchemy import Table, Column, Integer, String, DateTime
import os


class Review(BaseModel, Base):
    '''This is the 'Review' class'''
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
