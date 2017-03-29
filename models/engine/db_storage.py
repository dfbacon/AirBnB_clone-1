#!/usr/bin/python3
'''
This is the 'db_storage' module
'''
import sys
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import Base
from sqlalchemy import inspect


class DBStorage():
    """This is the 'DBStorage class"""
    __engine = None
    __session = None
    valid_models = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        '''This is the initialization method'''
        uname = os.environ["HBNB_MYSQL_USER"]
        upass = os.environ["HBNB_MYSQL_PWD"]
        host = os.environ["HBNB_MYSQL_HOST"]
        dbname = os.environ["HBNB_MYSQL_DB"]
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(uname, upass, host, dbname))
        self.__Session = sessionmaker()
        self.__Session.configure(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = self.__Session()

    def all(self, cls=None):
        '''This is the 'all' method'''
        query = {}
        if cls is not None:
            for instance in self.__session.query(cls):
                query.update(instance.id, instance)
            return (query)
        else:
            for cls in DBStorage.valid_models:
                cls = getattr(sys.modules["models"], cls)
                for instance in self.__session.query(cls):
                    query.update({instance.id: instance})
            return (query)

    def new(self, obj):
        '''This is the 'new' method'''
        self.__session.add(obj)

    def save(self):
        '''This is the 'save' method'''
        self.__session.commit()

    def delete(self, obj=None):
        '''This is the 'delete' method'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''This is the 'reload' method'''
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        Base.metadata.create_all(self.__engine)

    def close(self):
        self.__session.remove()
