#!/usr/bin/python3
"""
city class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class city.
    attributes:
        state_id(str)
        name(str)
    """
    state_id = ""
    name = ""
