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
def check_existing_users(name):
    '''
    Function that checks if a user account name already exists

    Args:
        name : the user account name
    '''

    return User.user_exist(name)


def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account

    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)


def display_users():
    '''
    Function that returns all the saved users 
    '''

    return User.display_user()


def create_credentails(user_name, name, password):
    '''
    Function to create a credential 

    Args:
        user_name : username for Password Locker
        name : the name of the account 
        password : the password for the account
    '''

    new_credentails = Credentials(user_name, name, password)

    return new_credentails


def save_credentials(credentials):
    '''
    Function to save a credentials

    Args:
        credentials : the credentials to be saved
    '''

    credentials.save_credentials()


def check_existing_credentials(name):
    '''
    Function that checks if a user credentials name already exists

    Args:
        name : the credentials name
    '''

    return Credentials.credentials_exists(name)


def display_credentials(password):
    '''
    Function that returns all the saved credentials
    '''

    return Credentials.display_credentials(password)


# def create_generated_password(name):
#     '''
#     Function that generates a password for the user 

#     Args:
#         name : the name of the account
#     '''
#     password = Credentials.generated_password()

#     return password
