#!/usr/bin/python3
"""
class place.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class Place.
    Attributes:
        city_id (str): City ID.
        user_id (str): User ID.
        name (str): place name.
        description (str): place description.
        number_rooms (int): Number of rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Number of guests.
        price_by_night (int): price per night.
        latitude (float): latitude.
        longitude (float): longitude.
        amenity_ids (list of str): list of amenities.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
