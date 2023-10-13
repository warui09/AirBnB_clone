#!/usr/bin/python3
from models.base_model import BaseModel

"""Definition of Review class"""
class Review(BaseModel):
    """Representation of this class
    Attributes:
    place_id (str): Initial will be empty
    user_id (str): initial will be empty
    text (str): initial will be empty
    """

    place_id = " "
    user_id = " "
    text = " "