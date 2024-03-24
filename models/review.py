#!/usr/bin/python3
"""
class Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review.
    Attributes:
        place_id(str).
        user_id(str).
        text(str).
    """
    place_id = ""
    user_id = ""
    test = ""
