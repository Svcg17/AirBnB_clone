#!/usr/bin/python3
""" The base_model module
"""
import uuid
import datetime
import copy


class BaseModel:
    """class BaseModel that defines all common attr/method
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for keys, value in kwargs.items():
                if keys == '__class__':
                    continue
                elif keys == "created_at" or keys == "updated_at":
                    formatt = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.datetime.strptime(value, formatt)
                setattr(self, keys, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Checks str"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

        def save(self):
            """ updates the public instance attributes
        """
            self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        """
        newdict = copy.deepcopy(self.__dict__)
        newdict["__class__"] = self.__class__.__name__
        newdict['created_at'] = self.created_at.isoformat()
        newdict['updated_at'] = self.updated_at.isoformat()
        return (newdict)
