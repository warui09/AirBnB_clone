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
from datetime import datetime

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
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()


    def get_objects(self, instance=''):
        """Gets the elements created by the console

        This method takes care of obtaining the information
        of all the instances created in the file `objects.json`
        that is used as the storage engine.

        When an instance is sent as an argument, the function
        takes care of getting only the instances that match the argument.

        Args:
            instance (:obj:`str`, optional): The instance to finds into
                the objects.

        Returns:
            list: If the `instance` argument is not empty, it will search
            only for objects that match the instance. Otherwise, it will show
            all instances in the file where all objects are stored.

        """
        objects = models.storage.all()

        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]

        return [str(val) for key, val in objects.items()]


    def do_default(self, line):
        """
        When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
            "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.

        """
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]

            if class_name in self.allowed_classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)


    def analyze_parameter_value(self, value):
        """Checks a parameter value for an update

        Analyze if a parameter is a string that needs
        convert to a float number or an integer number.

        Args:
            value: The value to analyze

        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value

    def emptyline(self) -> None:
        """Override the Cmd.emptyline() method
        """
        pass





if __name__ == '__main__':
    HBNBCommand().cmdloop()
