#!/usr/bin/python3

from models.base_model import BaseModel
"""Definition of the place class"""

class Place(BaseModel):
    """Representation of the class
    Attributes: 
    city_id (str): empty string - The city id
    user_id (str): empty string - The user's id
    name (str): Empty string
    description (str): empty string
    number_rooms (int): intitial = 0
    number_bathrooms (int): initial = 0
    max_guest (int): initial = 0
    price_by_night (int): initial = 0
    latitude (float): initial = 0.0
    longitue (float): initial = 0.0
    amenity_ids (str): empty list: it will be the list of Amenity.id later
    """
    city_id = " "
    user_id = " "
    name = " "
    description = " "
    number_rooms = " "
    number_bathrooms = " "
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = " "