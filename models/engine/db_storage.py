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


class DBStorage():
    """This is the 'DBStorage class"""
    __engine = None
    __session = None
    valid_models = {"Amenity": Amenity, "City": City, "State": State,
                     "Place": Place, "Review": Review,
                     "User": User, "PlaceAmenity": PlaceAmenity}

    def __init__(self):
        '''This is the initialization method'''
        usr = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_MYSQL_ENV')

        eng_str = "mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, host, db)

        self.__engine = create_engine(eng_str)
        Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = Session()
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        query_dict = {}
        if cls is None:
            for val_key, val_cls in self.valid_models.items():
                for instance in self.__session.query(val_cls):
                    query_dict[instance.id] = instance
        else:
            if (isinstance(cls, str) is True):
                for instance in self.__session.query(eval(cls)):
                    query_dict[instance.id] = instance
            else:
                for instance in self.__session.query(cls):
                    query_dict[instance.id] = instance
        return (query_dict)

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
        '''this si the 'close' method
        '''
        self.__session.remove()
