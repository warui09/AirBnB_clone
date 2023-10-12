#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
