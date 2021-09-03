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


def create_generated_password(name):
    '''
    Function that generates a password for the user 

    Args:
        name : the name of the account
    '''
    password = Credentials.generated_password()

    return password


def find_credentials(credentials_name, credentials_password):
    """
    function to fund credentials based on credentials name given
    """
    return Credentials.find_credentials(credentials_name, credentials_password)


def delete_credentials(name):
    """"
    Function to delete credentials no longer required

    Args:
        name : the name of the credentials
    """
    Delete = Credentials.delete_credentials()
# main function


def main():
    """
    Function to run the password locker app
    """
    print("               ____      __        ____     ____         __           ____      _____   _    __             ")
    print("              |  _ \    /  \      / ___|   / ____|      |  |       /     \   /  _____| | |  / /          ")
    print("              | |_) )  / __ \    / /___   / /____       |  |      |       | |  |       | | / /             ")
    print("              |  __/  / |__| \   \____  \ \____ \       |  |      |  |_|  | |  |       | | \ \            ")
    print("              | |    /   __   \   ____| |  ____| |      |  |_____ |       | |  |_____  | |  \ \           ")
    print("              |_|   /___|  |___\ |_____ / |______/      |________| \_____/   \______ | |_|   \_\       ")

    while True:
        """
        loop that is running the entire epplication 
        """
        print("""Short codes:
        Cu - Create a password Locker account \n
        Di - Display names of current password locker users \n
        Lg - Log into your account on password locker \n
        Ex - Exit the password locker account """)

        # taking short codes from the user
        short_code = input().lower()

        if short_code == "cu":

            print("\n")
            print(" New password locker account")
            print("*"*10)

            print("User name ...")
            user_name = input()

            print("password ...")
            user_password = input()

            # creating a new user and saving
            save_users(create_user(user_name, user_password))

            print("\n")
            print(
                f"Welcome {user_name} Your account has been created successfully! to Password Locker.")

        elif short_code == "du":
            """
            show names of present user
            """
            if display_users():
                print("\n")
                print("Below is the list of current users of password locker 👇")
                print("*"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("*"*10)
            else:
                print("\n")
                print("password locker does not have a user yet. \n  Be the first user")
                print("\n")

        elif short_code == "lg":
            """
            code to allow user log into password locker
            """
            print("\n")
            print("*"*10)
            print("Log in to your Password Locker Account")
            print("Enter the user name")
            user_name = input()

            print("Enter the password")
            user_password = input()

            if user_log_in(user_name, user_password) == None:
                print("\n")
                print("invalid user name or password, try again or create a new account")
                print("\n")

            else:

                user_log_in(user_name, user_password)
                print("\n")
                print(f"""Welcome {user_name} You have successfully logged into your credentials\n 
                use the following short codes to navigate""")

                while True:
                    """
                    loop for running functions post log-in
                    """
                    print(""" Short codes:
                    cc - add credentials  \n
                    dc - display credentials \n
                    gc - generate a credentials with autogenerate password \n
                    dlc - delete credentials \n
                    ext - exit credentials """)

                    # get short codes from user
                    short_code = input().lower()

                    if short_code == "cc":
                        print("\n")
                        print("New Credentials")
                        print("*"*10)

                        print("Name of the credentials ...")
                        credentials_name = input()

                        print("Password of the credentials ...")
                        credentials_password = input()

                        # creating and saving a new user
                        save_credentials(create_credentails(
                            user_name, credentials_name, credentials_password))

                        print("\n")
                        print(
                            f"Credentials for {credentials_name} have been successfully saved !")
                        print("\n")

                    elif short_code == "dc":
                        """
                        displaying credential name & password
                        """
                        if display_credentials(user_name):
                            print("\n")
                            print(f"{user_name}\'s credentials")
                            print("*"*10)

                            for credentials in display_credentials(user_name):
                                print(
                                    f"Account ..... {credentials.credentials_name}")
                                print(
                                    f"Password .... {credentials.credentials_password}")
                                print("*"*10)

                        else:
                            print("\n")
                            print("Sorry You do not have any account Match.")
                            print("\n")

                    elif short_code == "gc":
                        """
                        creating a credentials with autogenerated password
                        """
                        print("\n")
                        print("New Credentials")
                        print("*"*10)

                        print("Name of the credentials ...")
                        credentials_name = input()

                        # Save created credential with its generated password
                        save_credentials(Credentials(
                            user_name, credentials_name, (create_generated_password(credentials_name))))
                        print("\n")
                        print(
                            f"Credentials for {credentials_name} have been created and saved")
                        print("\n")

                    elif short_code == "dlc":
                        """
                        deleting credentials that are no longer needed
                        """
                        print("Enter name of credentials you no longer need")
                        credentials_name = input()

                        print("Enter password of credentials above")
                        credentials_password = input()

                        if check_existing_credentials(credentials_name):
                            delete_credentials_name = find_credentials(
                                credentials_name, credentials_password)
                            # print(f" {delete_credentials_name}")
                            print(
                                f"Your stored credentials for: {credentials_name} has been deleted Successfully")
                        else:
                            print(" ⚠️ That credentials does not exist ⚠️ ")

                    elif short_code == "ext":
                        print(
                            f"Thank you {user_name} for using password locker. see you soon ")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print(f""" {short_code} seems to be incorrect. \n 
                        please use the short codes provided""")
                        print("\n")
        elif short_code == "ex":
            """
            Exiting password locker
            """
            print("\n")
            print("Bye, have a good day .....")

            break

        else:
            print("\n")
            print(f""" Invalid entry please check amd try again. what is the the {short_code}? 
            please use the short codes """)
            print("\n")


if __name__ == '__main__':
    main()
