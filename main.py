

import re, getpass, os, csv


## First part 

print("1. New user /n2. Login ")

before_login = input("Select a number (from 1 to 2): ")

class new_user():
    
    def __init__(self, new_username, master_password, rep_passwd ):
        
        self.new_username = new_username
        self.master_password = master_password 

    def password_verification(self,master_password, rep_passwd):
        
        if (self.master_password = self.rep_passwd):
            pass 
        else:
            print("The master password is not the same with repeat password")

new_user1 = new_user(input("Enter your username:"), )  

## Second part 

print("This my password manager \n \n    1. Add new acount \n    2. See details of account ")

after_login = str(input("Select a number (from 1 to 2): "))

class new_account():
    def __init__(self, account_email, account_password):
        self.account_email = email
        self.account_password = password

