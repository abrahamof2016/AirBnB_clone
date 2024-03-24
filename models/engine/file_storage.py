#!/usr/bin/python3
"""
FileStorage module.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class FileStorage.
    Private Attributes:
        __filepath (str): file path to JSON file
        __objects (dict): dictionary of objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        all method dictionary of objects.
        returns:
            __objects - dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        adds object to dictionary __objects
        Args:
            obj (object): object to be added to a dictionary __objects
        """
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        json_str = json.dumps(obj_dict)

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            pass
