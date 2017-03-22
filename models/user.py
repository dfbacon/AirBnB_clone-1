#!/usr/bin/python3
'''
This is the 'user' module.
'''
from models import *
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import *
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
        '''This is the initialization method'''
        super().__init__(*args, **kwargs)
