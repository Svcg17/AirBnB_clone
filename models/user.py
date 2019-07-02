import models
from models.base_model import BaseModel
# from console import HBNBCommand


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
