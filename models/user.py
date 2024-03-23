#!/usr/bin/python3
"""
class user
It inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class user.
    attributes:
        email(string) - user's email
        password(str) - user's account password.
        first_name(str) - user's first name
        last_name(str) - user's last name
     """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
