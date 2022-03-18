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
        self.email = new_email

    def password_verification(self, master_password, rep_password):
        
        if (self.master_password == self.rep_password):
            pass 
        else:
            print("The master password is not the same with repeat password")
            return main().new_user1()

class login():

    def __init__(self, log_username, log_email, log_master_password, log_rep_password):
        self.log_username = log_username 
        self.log_email = log_email
        self.log_master_password = log_master_password
        self.log_rep_password = log_rep_password

class com(new_user, login):
    
    def ver(new, lo, master_password, log_master_password, log_rep_password):
        if (new.master_password == lo.log_master_password):
            if (lo.log_master_password == lo.log_rep_password):
                pass
            else: 
                print("Repeat password are wong")

        else

class new_account():

    def __init__(self, account_username, account_email, account_password, account_rep_password):
        
        self.account_username = account_username
        self.account_email = account_email
        self.account_password = account_password
        self.account_rep_password = account_rep_password

    def account_verification(self, account_password, account_rep_password):
        if (self.account_password == self.account_rep_password):
            pass

        else:
            return main().new_account_1()

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

        ## login to Account 
    elif before_login == 2:


        ## Make new Account
    
    elif before_login == 2:
        new_account_username = input("Enter your new account usernam: ")
        new_account_email = input("Enter your new account email")
        new_account_password = getpass("Enter your new account password")
        new_account_rep_password = getpass("Repeat password")

        new_account_1 = new_account(new_account_username, new_account_email, new_account_password, new_account_rep_password)
        new

        new_account_1.account_verification(new_account_1.account_password, new_account_1.account_rep_password)

if __name__ == '__main__':
    main()
