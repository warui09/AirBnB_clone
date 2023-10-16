#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import models
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.engine import file_storage
import re

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Airbnb project

    Attribute:
        prompt (str): This will be used as a cmd prompt
    """

    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "State": State,
        "Place": Place,
        "Review": Review
    }

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
        if not line:
            print("** class name missing **")
        elif line in HBNBCommand.valid_classes:
            new_instance = HBNBCommand.valid_classes[line]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line) -> None:
        """Prints the string representation of an instance
        based on the class name and id"""
        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            objectdict = models.storage.all()
            instance_key = "{}.{}".format(class_name, instance_id)
            if instance_key in objectdict:
                print(objectdict[instance_key])
            else:
                print("** no instance found **")

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

    def do_all(self, line):
        """Prints all string representations of all instances
        based or not on the class name"""
        args = line.split()
        all_objects = models.storage.all()
        result = []

        if not args:
            for key, value in all_objects.items():
                result.append(str(value))
            print(result)
        elif args[0] in models.classes:
            for key, value in all_objects.items():
                if args[0] == value.__class__.__name__:
                    result.append(str(value))
            print(result)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating an attribute (save the changes into a JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at a time.
        You can assume the attribute name is valid (exists for this model).
        The attribute value must be casted to the attribute type.
        """
        parsed_args = parse(arg)
        objectdict = models.storage.all()

        if len(parsed_args) < 2:
            print("** Usage: update <class name> <id> <attribute name> \"<attribute value>\" **")
            return False

        class_name = parsed_args[0]
        instance_id = parsed_args[1]

        if class_name not in HBNBCommand.__classes:
            print("** Class doesn't exist **")
            return False

        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key not in objectdict.keys():
            print("** No instance found **")
            return False

        if len(parsed_args) < 4:
            print("** Attribute name or value missing **")
            return False

        attribute_name = parsed_args[2]
        attribute_value = parsed_args[3]

        if attribute_name not in objectdict[instance_key].__class__.__dict__.keys():
            print(f"** Attribute '{attribute_name}' is not valid for this class **")
            return False

        attribute_type = type(objectdict[instance_key].__class__.__dict__[attribute_name])

        try:
            casted_value = attribute_type(attribute_value)
        except (ValueError, TypeError):
            print("** Attribute value could not be cast to the correct type **")
            return False

        setattr(objectdict[instance_key], attribute_name, casted_value)
        models.storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
