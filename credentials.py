import unittest
from random import choice 
import string 

"""
credentials class to create instances of the user's credentials 
"""

class Credentials:
    """
    this is a class that generates instances of credentials for the user
    """

    # start 
    credentials_list = [] # Empty list of the credentials

    def __init__(self, user_name, credentials_name, credentials_password):
        """
        __init__ method to  specify the attributes of a User object
        
        Args:
            user_name = user name
            credentials_name = the name of the credentials acccount
            credentials_password = the password of the account
        """
        self.user_name = user_name
        self.credentials_name = credentials_name
        self.credentials_password = credentials_password

    def save_credentials(self):
        """
        method through which the application saves the user credentials to credentials list
        """
        Credentials.credentials_list.append(self)