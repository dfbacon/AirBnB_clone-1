#!/usr/bin/python3
'''
This is the 'base_model' module.
'''
import datetime
import uuid
import models
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

try:
    e = os.environ.get('HBNB_TYPE_STORAGE')
    if e == "db":
        Base = declarative_base()
    else:
        Base = object
except:
    Base = object


class BaseModel():
    """The base class for all storage objects in this project"""

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.datetime.now(),
                            nullable=False)
        updated_at = Column(DateTime, default=datetime.datetime.now(),
                            onupdate=datetime.datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """method to update self"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        if os.environ.get('HBNB_TYPE_STORAGE') != "db":
            dupe["created_at"] = str(dupe["created_at"])
            if ("updated_at" in dupe):
                dupe["updated_at"] = str(dupe["updated_at"])
                dupe["__class__"] = type(self).__name__
        try:
            del(self.__dict__['_sa_instance_state'])
        except KeyError:
            pass
        return dupe

    def delete(self):
        '''delete current instance'''
        models.storage.delete(self)
