#!/usr/bin/python3
"""
Defines a BaseModel that defines all common attributes and
methods for other classes
"""

import datetime
import time
import uuid
import models

class BaseModel:
    """
    Defines a BaseModel that defines all common attributes and
    methods for other classes
    Public instance attributes:
        id: string assigned uuid whenever an instance is created
        created_at:  datetime - assign with the current datetime
                     when an instance is created
        updated_at: datetime - assign with the current datetime
                    when an instance is created and it will be updated
    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    Public instance methods:
        save(self): updates the public instance attribute updated_at
                    with the current datetime
        to_dict(self): returns a dictionary containing all keys/values
                    of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a base model instance with the following attributes:
        id:
            unique id generated using uuid
        created_at:
            time when the instance was created
        updated_at:
            time when the instance was updated
        Objetcs will also be instantiated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if len(kwargs) != 0:
           tform = "%Y-%m-%dT%H:%M:%S.%f"
           for a, b in kwargs.items():
             if a == "created_at" or a == "updated_at":
               self.__dict__[a] = datetime.strptime(b, tform)
             else:
               self.__dict__[a] = b
        else:
          models.storage.new(self)


    def __str__(self):
        """
        Prints: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict[__class__] = self.__class__.__name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict #so that it returns what you docummented --this is an added line
