#!/usr/bin/python3
from models import *


class User(BaseModel):
    '''This is the 'User' class'''
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
