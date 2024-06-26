"""
validations/user_validations.py

This module defines validation functions related to user operations.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - models.users.User: Pydantic model for representing user data.
    - services.userService.collection: MongoDB collection for storing user data.

Functions:
    - sign_up_check_user: Check if user data is valid for sign up.


"""

from fastapi import HTTPException
from models.users import User
from services.userService import collection


def sign_up_check_user(new_user: User):
    """
    Check if user data is valid for sign up.

    Args:
        new_user (User): New user data.

    Returns:
        User: Validated user data.

    Raises:
        HTTPException: If an error occurs during validation.
    """
    print(new_user)
    result = list(collection.find({"name": new_user.name, "password": new_user.password}))
    if len(result) != 0:
        raise HTTPException(status_code=401, detail="Name or password is incorrect")
    else:
        return new_user


def validate_id(id_value):
    try:
        id_value = int(id_value)
        if id_value > 0:
            return True,
        else:
            return False,
    except ValueError:
        return False,


import re


def validate_username(username):
    if len(username) < 3 or len(username) > 15:
        return False,
    if not re.match("^[A-Za-z][A-Za-z0-9]*$", username):
        return False,
    return True,
