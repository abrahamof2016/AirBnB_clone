#!/usr/bin/python3
"""
User module.
"""
import models


class User(models.base_model.BaseModel):
    """
    Class User.
    Attributes:
        email (str): User email.
        password (str): User password.
        first_name (str): User first name.
        last_name (str): User last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
