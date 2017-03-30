#!/usr/bin/python3
'''
This is the 'review' method.
'''
from models.base_model import BaseModel, Base, Table, Column, String
from sqlalchemy import ForeignKey
from os import getenv


class Review(BaseModel, Base):
    '''This is the 'Review' class'''
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization method'''
        super().__init__(*args, **kwargs)
