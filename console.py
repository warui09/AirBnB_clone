#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
from models import base_model

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Airbnb project
    """
    prompt = '(hbnb) '

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

    def do_create(self, line) -> None:
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        if len(line) == 0:
            print("** class name missing **")
        elif hasattr(base_model, line):
            new_instance = eval(f'base_model.{line}()')
            #new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
