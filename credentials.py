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
    credentials_list = []  # Empty list of the credentials

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
    # generating password for the user

    @classmethod
    def generated_password(cls):
        """
        this method will generate a random alphanumeric password for the user 
        """
        # length of password to be generated
        size = 10

        # random alphanumeric generation
        alphanumeric = string.ascii_lowercase + string.digits + string.ascii_uppercase

        # now to create the password
        password = "".join(choice(alphanumeric) for num in range(size))

        return password

    # method to display the credentials
    @classmethod
    def display_credentials(cls, user_name):
        """
        method that will return the credentials list

        Args:credentials_email = the email of the credentials account to be linked with the account
            password  : the user password
        """
        user_credentials_list = []

        for credentials in cls.credentials_list:
            if credentials.user_name == user_name:
                user_credentials_list.append(credentials)

        return user_credentials_list

    @classmethod
    def credentials_exists(cls, credentials_name):
        """
        method to check existense of a credentials

        Args
            name: name of credentials to be searched

        Returns:
            Boolean: true/ false subject to whether the credentials exist
        """

        for credentials in cls.credentials_list:
            if credentials.credentials_name == credentials_name:
                return True

        return False

    # method to find credentials
    @classmethod
    def find_credentials(cls, credentials_name, credentials_password):
        """
        method that takes in credentials name and returns the credentials entry saved.

        Args
            name: is the name of the platform e.g facebook that a user has saved in the application
        Returns :
            credentials name and password that matches the input given.
        """

        for credentials in cls.credentials_list:
            if credentials_name == credentials_name and credentials_password == credentials_password:
                return credentials

    # deleting credentials
    @classmethod
    def delete_credentials(credentials_name, credentials_password):
        """
        method that deletes credentials account that user no longder needs
        """
        Credentials.credentials_list.remove()


if __name__ == '__main__':
    unittest.main()
