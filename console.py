#!/usr/bin/python3
""" Cmd line entry point """
import models
from models import storage
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):
    """ Cmd line interpreter """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ quitting implementation """
        raise SystemExit

    def do_EOF(self, args):
        """ EOF implementation """
        return True
  
    def emptyline(self, args):
        """ empty implementation """
            pass

    HBNBCommand().cmdloop():
        """ infinite """

           
