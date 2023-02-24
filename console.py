#!/usr/bin/python3
"""_summary_
    """
import cmd
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel

classs = ['BaseModel',]


def split(arg):
    if not arg:
        print("** class name missing **")
        return None, None
    class_name = arg.split()[0]
    if class_name not in ['BaseModel', 'OtherModel']:
        print("** class doesn't exist **")
        return None, None
    if len(arg.split()) < 2:
        print("** instance id missing **")
        return None, None
    given_id = arg.split()[1]
    return class_name, given_id


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
        if class_name not in ['BaseModel', 'OtherModel']:
            print("** class doesn't exist **")
            return
        new_object = BaseModel()
        new_object.save()
        print(new_object.id)

    def do_show(self, arg):
        class_name, given_id = split(arg)
        if not class_name or not given_id:
            return
        key = class_name + '.' + given_id
        obj = storage.all()

        if key not in obj:
            print("** no instance found **")
        else:
            instance = obj[key]
            print(instance)

    def do_destroy(self, arg):
        class_name, given_id = split(arg)
        if not class_name or not given_id:
            return
        key = class_name + '.' + given_id
        obj = storage.all()

        if key not in obj:
            print("** no instance found **")
        else:
            del obj[key]
            storage.save()

    def do_all(self, arg):
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in ['BaseModel', 'OtherModel']:
            print("** class doesn't exist **")
            return
        objs = storage.all().values()
        print([str(obj) for obj in objs if type(obj).__name__ == class_name])

    def do_update(self, arg):
        class_name, given_id = split(arg)
        if not class_name or not given_id:
            return
        if len(arg.split()) < 3:
            print("** attribute name missing **")
        if len(arg.split()) < 4:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
