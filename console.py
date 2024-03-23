#!/usr/bin/python3
"""
custom command interpreter.
"""
import sys
import cmd
import shlex
import models
from models.base_model import BaseModel
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

    def do_EOF(self, line):
        """
        exit the program when invoked.
        """
        print()
        return True

    def do_create(self, line):
        """
        creates a new instance of BaseModel,
        saves it (to the JSON file),
        and prints instance id.
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = eval("{}()".format(args[0]))
            print(obj.id)
            models.storage.save()

    def do_show(self, line):
        """
        prints the string representation of an instance.
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.
        Save the change into the JSON file.
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                objs.pop(key)
                del obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
        prints all string representation of all instances
        based or not on the class name.
        """
        args = parse(line)
        objs = models.storage.all()
        obj_list = []
        if len(args) >= 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, obj in objs.items():
                    if key.startswith(args[0]):
                        obj_list.append(obj.__str__())
                    print(obj_list)
        else:
            for obj in objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id and attr name.
        """
        args = parse(line)
        objs = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    try:
                        eval(args[3])
                    except (SyntaxError, NameError):
                        args[3] = "'{}'".format(args[3])
                    setattr(obj, args[2], eval(args[3]))
                    obj.save()
            except KeyError:
                print("** no instance found **")


def parse(line):
    """
    parse a string and return a list of parsed arguments.
    """
    return shlex.split(line)
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
