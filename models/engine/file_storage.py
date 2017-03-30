#!/usr/bin/python3
'''
This is the 'file_storage' module.
'''
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import os


class FileStorage:
    '''This is the 'FileStorage' class'''
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''This is the initialization method'''
        self.__models_available = {"User": User, "BaseModel": BaseModel,
                                   "Amenity": Amenity, "City": City,
                                   "Place": Place, "Review": Review,
                                   "State": State}
        self.reload()

    def all(self, cls=None):
        '''This is the 'all' method'''
        if cls is None:
            return(FileStorage.__objects)
        else:
            result = {}
            for key, value in FileStorage.__objects.items():
                if value.__class__.__name__ == cls:
                    result[key] = value
            return(result)

    def new(self, obj):
        '''This is the 'new' method'''
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        '''This is the 'save' method'''
        store = {}
        for key in FileStorage.__objects.keys():
            store[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, mode="w+", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        '''This is the 'reload' method'''
        FileStorage.__objects = {}
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                temp = json.load(fd)
        except Exception as e:
            return
        for key in temp.keys():
            cls = temp[key].pop("__class__", None)
            if cls not in self.__models_available.keys():
                continue
            FileStorage.__objects[key] = self.__models_available[cls](
                **temp[key])

    def delete(self, obj=None):
        '''This is the 'delete' method'''
        if obj:
            FileStorage.__objects.pop(obj.id, None)
            self.save()

    def close(self):
        '''This is the 'close' method'''
        self.reload()
