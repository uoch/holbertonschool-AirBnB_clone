#!/usr/bin/python3
"""_summary_
    """
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import json
def update_filestorage(*args):
    for cls in args:
        if cls.__name__ not in FileStorage.__objects.keys():
            FileStorage.__objects[cls.__name__] = {}

        for obj in cls.all().values():
            key = "{}.{}".format(cls.__name__, obj.id)
            FileStorage.__objects[cls.__name__][key] = obj

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
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                try:
                    objs_dict = json.load(f)
                except json.JSONDecodeError:
                    objs_dict = {}
                for key, value in objs_dict.items():
                    cls_name = key.split('.')[0]
                    obj = eval(cls_name)(**value)
                    self.new(obj)
        else:
            pass
