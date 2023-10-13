#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import models
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
import re

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Airbnb project

    Attribute:
        prompt (str): This will be used as a cmd prompt
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

    def do_show(self, line) -> None:
        """Prints the string representation of an instance
        based on the class name and id"""
        args = line.split()
        class_name, instance_id = args
        if !class_name:
            print("** class name missing **")
        elif !hasattr(base_model, class_name):
            print("** class doesn't exist **")
        elif !instance_id:
            print("** instance id missing **")
        else:
            print("string representation")

    def do_destroy(self, arg):
        """Deletes an instance based on 
        the class name and id"""
        parsed_args = parse(arg) #Start working on the class names
        #parse function is used to break down arg input to the relevant components
        objectdict = models.storage.all()

        if len(parsed_args) == 0:
            print("** class name missing **")
        elif parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(parsed_args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(parsed_args[0], parsed_args[1]) not in objectdict.keys():
            print("** no instance found **")
        else:
            del objectdict["{}.{}".format(parsed_args[0], parsed_args[1])]
            models.storage.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
