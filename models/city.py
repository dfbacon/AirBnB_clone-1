#!/usr/bin/python3
from models import *
from sqlalchemy import Table, Column, Integer, String, DateTime


class City(BaseModel, Base):
    '''This is the 'City' class'''
    if Base is not object:
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
