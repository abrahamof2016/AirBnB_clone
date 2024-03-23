#!/usr/bin/python3
"""
BaseModel module
"""
import uuid
import datetime
import models


class BaseModel:
    """
    class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        A method to initialize instances of class BaseModel.
        Args:
            args (tuple): arguments
            kwargs (dict): dictionary of arguments
        """
        if kwargs:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        return string representation of BaseModel.
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        save method of BaseModel updates the public instance attribute
        uptadte_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        creates dictionary with all key/values of __dict__ of the instance
        returns:
            dictionary of instance key-value pairs
        """
        base_dict = dict(self.__dict__)
        base_dict['__class__'] = type(self).__name__
        base_dict['created_at'] = base_dict['created_at'].isoformat()
        base_dict['updated_at'] = base_dict['updated_at'].isoformat()
        return base_dict
