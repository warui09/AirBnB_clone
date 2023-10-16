#!/usr/bin/python3
"""
BaseModel that all other classes inherit from
"""

import datetime
import uuid


class BaseModel:
    """
    Base class for all other classes. Contains common
    attributes and methods for all classes
    Attributes:
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when
            an instance is created
        updated_at: datetime - assign with the current datetime when
            an instance is created and it will be updated
    Methods:
        save(self): Updates the public instance attribute updated_at
            with the current datetime
        to_dict(self): Returns a dictionary containing all keys/values
            of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a base model instance with the following attributes:
        id: unique id generated using uuid
        created_at: time when the instance was created
        updated_at: time when the instance was updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:  # Check if keyword arguments are provided
            # If 'created_at' or 'updated_at' is in kwargs, convert them to datetime
            if "created_at" in kwargs:
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
                del kwargs["created_at"]
            if "updated_at" in kwargs:
                self.updated_at = datetime.datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
                del kwargs["updated_at"]
            # Assign other key-value pairs from kwargs to instance attributes
            for key, value in kwargs.items():
                setattr(self, key, value)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        This method should be further extended to save the instance to a storage system.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        This method should be further extended to include '__class__' and '__str__' keys.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())
