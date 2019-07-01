#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    This class has public attributes defining User and will use
    FileStorage to handle both serialization and deserialization
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
