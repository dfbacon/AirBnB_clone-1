#!/usr/bin/python3
'''
This is the 'file_storage' module.
'''
import json
from datetime import datetime
from models import *


class FileStorage:
    '''This is the 'FileStorage' class'''
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''This is the initialization method'''
        self.reload()

    def all(self, cls=None):
        '''This is the 'all' method'''
        return FileStorage.__objects

    def new(self, obj):
        '''This is the 'new' method'''
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        '''This is the 'save' method'''
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_json()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        '''This is the 'reload' method'''
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = {}
                temp = json.load(fd)
                for k in temp.keys():
                    cls = temp[k].pop("__class__", None)
                    cr_at = temp[k]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[k]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(temp[k])
        except Exception as e:
            pass

    def delete(self, obj=None):
        '''This is the 'delete' method'''
        if obj is not None:
            try:
                del(self.__objects[obj])
            except:
                pass

    def close(self):
        '''This is the 'close' method'''
        self.save()
