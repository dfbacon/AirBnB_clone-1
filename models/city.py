#!/usr/bin/python3
'''
This is the 'city' module.
'''
from models import *
from models.base_model import BaseModel, Base
from sqlalchemy import *


class City(BaseModel, Base):
    '''This is the 'City' class'''
    if Base is not object:
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization method'''
        super().__init__(*args, **kwargs)
