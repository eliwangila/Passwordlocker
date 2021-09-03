#!/usr/bin/env python3.7

from user import User
from credentials import Credentials

"""
Run module 

File that runs the application
import the two class modules to be run
"""


def create_user(name, password):
    """
    function that creates a user account

    Args
        name: name of choice by user for their account
        password: select password that user wants for their account
    """

    new_user = User(name, password)

    return new_user


def save_users(user):
    """
    Function to save the user account created

    Args
        user: the user account to be saved 
    """

    user.save_user()