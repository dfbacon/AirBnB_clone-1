#!/usr/bin/python3
'''
This is the 'review' method.
'''
from models import *
from models.base_model import BaseModel, Base
from sqlalchemy import *


class Review(BaseModel, Base):
    '''This is the 'Review' class'''
    if Base is not object:
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
