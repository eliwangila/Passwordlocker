import unittest
from credentials import Credentials  # impoting the credentials class


class User:
    """
    Class that generates new instances of user accounts 
    """

    # start
    user_list = []  # Empty user list

    def __init__(self, user_name, user_password):
        '''
        __init__ method to define the properties of a User object

        Args:
            user_name : the name of the user 
            user_password : the user's password
        '''

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        """
        saving a user to the user list
        """
        User.user_list.append(self)

        # finding a user's credentials
    @classmethod
    def find_credentials(cls, name):
        """
        checks correct importation

        Args:
            name: credentials name

        Returns:
            Boolean : True / False depending on if the credential exists or not
        """

        # to search in the user list
        for credentials in Credentials.credentials_list:
            if credentials.credentials_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
        """
        method for user to log into their accounts

        Args:
            name : name of user
            password : password for the user

        Returns: 
            credentials list if name of user matches name of password
            False: if the name or password incorrect
        """

        # search for the user list
        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credentials.credentials_list

        return False

    @classmethod
    def display_user(cls):
        """
        method that returns the user list 
        """

        return cls.user_list

    @classmethod
    def user_exists(cls, name):
        """
        method that checks if a user exists in the user list
        Args:
            name: name of the user to search 

        Returns:
            Boolean: true/false depending on whether  user exists
        """

        for user in cls.user_list:
            if user.user_name == name:
                return True

        return False


if __name__ == '__main__':
    unittest.main()
