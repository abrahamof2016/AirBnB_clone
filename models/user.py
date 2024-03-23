"""
user module.
"""
import models
import BaseModel from models
class User(models.BaseModel):
    """
    class user.
    Inherits from BaseModel.
    Attr:
        email(str): empty sting.
        password(str): empty string.
        first_name(str): empty string.
        last_name(str): empty string.

    """
    emial = ""
    password = ""
    first_name = ""
    last_name = ""
