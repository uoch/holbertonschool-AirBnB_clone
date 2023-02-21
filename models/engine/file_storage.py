#!/usr/bin/python3
"""_summary_
    """
import os
from datetime import datetime
from models.base_model import BaseModel
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        return self.__objects

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            obj_dict = {}
            for key, obj in FileStorage.__objects.items():
                obj_dict[key] = obj.to_dict()
            return json.dump(obj_dict, f)

    def reload(self):
        """
1 Check if __file_path is not None
2 Open the file at __file_path
3 Load the JSON data from the file into a new dictionary loaded_objs
4 Iterate through loaded_objs dictionary items
5 Get the class name and ID from the dictionary key
6 Use the class name to look up the class type and create a new instance
with the data from the dictionary value
7 Add the new instance to the __objects dictionary
using the key class name and ID
    """
        try:
            with open(self.__file_path, 'r') as f:
                bigob = json.load(f)
                for key, obj in bigob.items():
                    class_name = key.split('.')[0]
                    obj = eval(class_name)(**obj)
                    self.__objects[key] = obj
        except FileNotFoundError:
        	pass
