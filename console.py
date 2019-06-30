#!/usr/bin/python3
""" Cmd line entry point """
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ Cmd line interpreter """
    prompt = "(hbnb) "

    def emptyline(self):
        """ empty implementation """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    do_EOF = do_quit

    def do_create(self, args=None):
        """Creates a new instance of BaseModel, s
        aves it (to the JSON file) and prints the id"""
        try:
            if not args:
                print("** class name missing **")
            else:
                newinstance = args.split()
                newinstance = eval(args)()
                newinstance.save()
                print(newinstance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args=None):
        """Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        line = args.split()
        if line[1] == instance.id:
            print(instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
