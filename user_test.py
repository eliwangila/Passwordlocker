import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    """
    test class that tests cases for the User class

    Args:
        unittest.Testcase: class that helps create test cases
    """
    def setUp(self):
        """
        set up method to run before each test case
        """

        # create a user object
        self.new_user = User("ekirapa","e347308")

    def tearDown(self):
        """
        method to clean up after each test
        """
        User.user_list = []

    def test_init(self):
        """
        to test if object is properly initialised
        """

        self.assertEqual( self.new_user.user_name, "ekirapa")
        self.assertEqual( self.new_user.user_password, "e347308")