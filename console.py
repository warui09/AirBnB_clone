#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import models
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Airbnb project

    Attribute:
        prompt (str): This will be used as a cmd prompt
    """
    prompt = '(hbnb) '
    __classes{
        "BaseModel",
    }

    def do_quit(self, line) -> None:
        """Quit command to exit the program
        """
        exit(0)

    def do_EOF(self, line) -> None:
        """Quit command to exit the program
        """
        print()
        exit(0)

    def emptyline(self) -> None:
        """Override the Cmd.emptyline() method
        """
        pass

    def do_create(self):
        """used as: create <class>
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
         Ex: $ create BaseModel"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
