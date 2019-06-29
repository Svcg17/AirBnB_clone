#!/usr/bin/python3
""" The file_storage module
"""
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """ A FileStorage class

    Attributes:
        ...
    """
    def __init__(self):
        self.file_path = "file.json"
        self.objects = {}

    @property
    def file_path(self):
        """ file_path getter method
        """
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path

    @property
    def objects(self):
        """ objects getter method
        """
        return self.__objects

    @objects.setter
    def objects(self, objects):
        self.__objects = objects

    def all(self):
        """ returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        keyy = obj.__class__.__name__ + "." + obj.id
        self.__objects[keyy] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_pddath)
       """
        newdict = {}
        for key in self.__objects:
            newdict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode='w') as f:
            json.dump(newdict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        if path.isfile(self.__file_path):
            content = {}
            with open(self.__file_path, mode='r') as f:
                content = json.load(f)
                for k, v in content.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
