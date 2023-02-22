#!/usr/bin/python3
"""_summary_
    """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        print()
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
