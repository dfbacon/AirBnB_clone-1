#!/usr/bin/python3
from models import *
from sqlalchemy import Table, Column, Integer, Float, String, Datetime
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''This is the 'User' class'''
    if Base is not object:
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        places = [""]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
