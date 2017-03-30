#!/usr/bin/python3
'''
This is the 'db_storage' module
'''
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, scoped_session)
from os import getenv
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class DBStorage():
    """This is the 'DBStorage class"""
    __engine = None
    __session = None
    __Session = None

    def __init__(self):
        '''This is the initialization method'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')))
        self.__models_available = {"User": User, "Amenity": Amenity,
                                   "City": City, "Place": Place,
                                   "Review": Review, "State": State}
        if getenv('HBNB_MYSQL_ENV', 'not') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        if cls:
            for key in self.__session.query(self.__models_available[cls]):
                objects[key.__dict__['id']] = key
        else:
            for value in self.__models_available.values():
                i = self.__session.query(value).all()
                if i:
                    for key in i:
                        objects[key.__dict__['id']] = key
        return(objects)

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
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        '''this si the 'close' method
        '''
        self.__session.remove()
