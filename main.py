## Password Manager

import re, os, csv
from getpass import getpass

## First part 

print("1. New user \n2. Login ")

before_login = int(input("Select a number (from 1 to 2): "))

class new_user():
    
    def __init__(self, new_username, new_email, master_password, rep_password ):
        
        self.new_username = new_username
        self.master_password = master_password 
        self.rep_password = rep_password
        self.email = email

    def password_verification(self, master_password, rep_password):
        
        if (self.master_password == self.rep_password):
            pass 
        else:
            print("The master password is not the same with repeat password")
            return main().new_user1()
    def email_verification(self, email):
        pattern = r"@....com"

        if re.search(pattern, self,email):
            pass 
        else:
            print("Your haven't the @gmail.com or something like that")

class new_account():

    def __init__(self, account_email, account_password):
    
        self.account_email = email
        self.account_password = password

def main():

    if before_login == 1:

        ## User input 
        new_username_input = input("Enter your username: ")
        new_master_password_input = getpass("Enter your master password: ")
        new_rep_password_input = getpass("Repeat your master password: ")
        new_email_input = input("Enter your email: ")
        new_user1 = new_user(new_username_input, new_email_input, new_master_password_input, new_rep_password_input)
    
        ## Data verification 
        new_user1.password_verification(new_user1.master_password, new_user1.rep_password)
        new_user1.email_verification(new_user1.email)

## Second part 

    print("\n \n    1. Add new acount \n    2. See details of account ")

    after_login = str(input("Select a number (from 1 to 2): "))


if __name__ == '__main__':
    main()
