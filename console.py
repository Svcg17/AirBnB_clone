#!/usr/bin/python3
""" Cmd line entry point """
import cmd
from cmd import Cmd

class HBNBCommand(cmd.Cmd):
    """ Cmd line interpreter """
    prompt = "(hbnb) "

    def do_exit(self, args):
        """ EOF implementation """
        return True 
    
    def emptyline(self):
        """ empty implementation """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n') 

    def do_quit(self, args):
        """Quit command to exit the program 
        """
        raise SystemExit

    do_EOF = do_exit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
