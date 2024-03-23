"""
user module.
"""
from models.base_model import BaseModel
class User(BaseModel):
    """
    class user.
    Inherits from BaseModel.
    Attr:
        email(str): empty sting.
        password(str): empty string.
        first_name(str): empty string.
        last_name(str): empty string.

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
