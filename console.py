#!/usr/bin/python3
"""_summary_
    """
import cmd
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class_dict = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}
lists =['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

def split(arg):
    if not arg:
        print("** class name missing **")
        return None, None
    class_name = arg.split()[0]
    if class_name not in class_dict:
        print("** class doesn't exist **")
        return None, None
    if len(arg.split()) < 2:
        print("** instance id missing **")
        return None, None
    given_id = arg.split()[1]
    return class_name, given_id


def check_in_bigobj(class_name, given_id):
    key = class_name + '.' + given_id
    obj = storage.all()
    if key not in obj:
        print("** no instance found **")
        return None
    else:
        instance = obj[key]
        print(instance)
        return instance


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        print()
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in lists:
            print("** class doesn't exist **")
            return
        new_object = eval(arg)()
        new_object.save()
        print(new_object.id)

    def do_show(self, arg):
        class_name, given_id = split(arg)
        if not class_name or not given_id:
            return
        instance = check_in_bigobj(class_name, given_id)
        if not instance:
            return
        print(instance)

    def do_destroy(self, arg):
        class_name, given_id = split(arg)
        if not class_name or not given_id:
            return
        instance = check_in_bigobj(class_name, given_id)
        if not instance:
            return
        key = class_name + '.' + given_id
        obj = storage.all()
        del obj[key]
        storage.save()

    def do_all(self, arg):
        if arg:
            class_name = arg.split()[0]
            if class_name not in class_dict:
                print("** class doesn't exist **")
                return
            objs = storage.all().values()
            objs_filtered = [str(obj) for obj in objs if type(
                obj).__name__ == class_name]
            print(objs_filtered)
        else:
            objs = storage.all().values()
            objs_filtered = [str(obj) for obj in objs]
            print(objs_filtered)

    def do_update(self, arg):
        class_name, given_id = split(arg)
        if not class_name or not given_id:
            return
        if len(arg.split()) < 3:
            print("** attribute name missing **")
            return
        if len(arg.split()) < 4:
            print("** value missing **")
            return
        instance = check_in_bigobj(class_name, given_id)
        if not instance:
            return
        attr_name = arg.split()[2]
        attr_value = arg.split()[3]
        setattr(instance, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
