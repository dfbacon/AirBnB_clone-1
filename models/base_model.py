#!/usr/bin/python3
'''
This is the 'base_model' module.
'''
from datetime import datetime
import uuid
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, DateTime

if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel():
    """The base class for all storage objects in this project"""

    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(timezone=True), default=datetime.now(),
                            nullable=False)
        updated_at = Column(DateTime(timezone=True), default=datetime.now(),
                            nullable=False, onupdate=datetime.now)

    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if args:
            kwargs = args[0]
        if kwargs:
            flag_id = False
            flag_created_at = False
            for key in kwargs.keys():
                if key == "created_at" or key == "updated_at":
                    if key == "created_at":
                        flag_created_at = True
                    if not isinstance(kwargs[key], datetime):
                        kwargs[key] = datetime(
                            *self.__str_to_numbers(kwargs[key]))
                elif key == "id":
                    flag_id = True
                setattr(self, key, kwargs[key])
            if not flag_created_at:
                self.created_at = datetime.now()
            if not flag_id:
                self.id = str(uuid.uuid4())
        elif not args:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())

    def save(self):
        """method to update self"""
        self.__dict__["updated_at"] = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe.pop('_sa_instance_state', None)
        dupe["created_at"] = dupe["created_at"].isoformat()
        if ("updated_at" in dupe):
            dupe["updated_at"] = dupe["updated_at"].isoformat()
        dupe["__class__"] = type(self).__name__
        return (dupe)

    def delete(self):
        '''delete current instance'''
        models.storage.delete(self)
