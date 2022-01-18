## Password Manager

import re, os, csv
from getpass import getpass

## First part 

print("1. New user \n2. Login ")

before_login = int(input("Select a number (from 1 to 2): "))

class new_user():
    
    def __init__(self, new_username, master_password, rep_password ):
        
        self.new_username = new_username
        self.master_password = master_password 
        self.rep_password = rep_password

    def password_verification(self, master_password, rep_password):
        
        if (self.master_password == self.rep_password):
            pass 
        else:
            print("The master password is not the same with repeat password")


if before_login == 1:

    new_username_input = input("Enter your username: ")
    new_master_password_input = getpass("Enter your master password: ")
    new_rep_password_input = getpass("Repeat your master password: ")

    new_user1 = (new_username_input, new_master_password_input, new_rep_password_input)
    
    new_user1.password_verification(new_user1.new_master_password_input, new_user1.new_rep_password_input)


## Second part 

print("\n \n    1. Add new acount \n    2. See details of account ")

after_login = str(input("Select a number (from 1 to 2): "))

class new_account():
    def __init__(self, account_email, account_password):
        self.account_email = email
        self.account_password = password

