#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage. If cls is specified,
        returns a dictionary of models of the specified class.
        """
        if cls is None:
            return FileStorage.__objects

        filtered_objects = {}
        for key, value in FileStorage.__objects.items():
            if type(value) == cls:
                filtered_objects[key] = value
        return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.all()[key] = obj


    def save(self, obj):
        """Serializes obj to JSON file"""
        all_objs = self.all()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        all_objs[key] = obj.to_dict()
        self.__objects = all_objs
        self.save_to_file()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    obj = classes[cls_name](**val)
                    self.all()[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside. If obj is equal to None,
        the method does nothing.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.all().pop(key, None)

