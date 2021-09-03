import unittest # Importing the unittest module
from credentials import Credentials # Importing the Credentials  class


class TestCredentials(unittest.TestCase):
    """
    class for test that defines test cases for the credentials module

    Args:
        unittest.TestCase : test class for python that helps create test cases for the application 
    """
    def setUp(self):
        """
        set up method will run before each test case
        """
        # creating the credential object
        self.new_credentials = Credentials("ekirapa","gmail","e@g.c")

    def tearDown(self):
        """
        the tearDown method will help to clean up after every test case is run 
        """
        Credentials.credentials_list = []

    def test_init(self):
        """
        testcase: testing to see whether object is well initialised
        """
        self.assertEqual( self.new_credentials.user_name, "ekirapa")
        self.assertEqual( self.new_credentials.credentials_name, "gmail")
        self.assertEqual( self.new_credentials.credentials_password, "e@g.c")

    # def test_save_credentials(self):
    #     """
    #     test to see whether user is saved to user list
    #     """
        
    #     self.new_credentials.save_credentials()

    #     self.assertEqual( len(Credentials.credentials_list), 1)

    # def test_save_multiple_credentials(self):
    #     """
    #     test case: checking to see if multiple credentials can be saved to credentials list
    #     """

    #     generated_password = self.new_credentials.generated_password()

    #     self.assertEqual ( len(generated_password), 10)
    
    # def test_display_credentials(self):
    #     """
    #     test to see if user can list all saved credentials
    #     """