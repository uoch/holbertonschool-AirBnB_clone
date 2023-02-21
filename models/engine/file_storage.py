#!/usr/bin/python3
"""_summary_
    """


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
            json.dump(obj_dict, f)

    def reload(self):
        if __file_path is not None:
            with open('data.json', 'r') as f:
                self.__objects = json.load(f)
        else:
            exit()
