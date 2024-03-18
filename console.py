#!/usr/bin/python3
"""
custom command interpreter.
"""
import sys
import cmd
# import models
# from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from modlels.amenity import Amenity
# from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand.
    """

    prompt = '(hbnb) '
    methods = ['all', 'show', 'count', 'update', 'destroy']
    classes = [
            'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

    def emptyline(self):
        """
        modifies the dafualt empty line behaviour of Cmd class.
        no command is executed for empty line.
        """
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def d_EOF(self, line):
        """
        exit the program when invoked.
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
