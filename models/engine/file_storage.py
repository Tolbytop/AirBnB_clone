#!/usr/bin/python3
"""
This module writes a class that serializes instances to a json file
and serializes instances to a json file
"""
import json
import os


class FileStorage:
    """
    This class serializes instances to a json file
    and deserializes json file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the json file """
        to_dict = {}
        for key, value in self.__objects.items():
            to_dict.update({key: value.to_dict()})
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(to_dict, file, sort_keys=True)

    def reload(self):
        """
        deserializes the json file to __objects
        only if the json file exists, otherwise, do nothing
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                from_json = json.load(file)
                for value in from_json.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        else:
            return
