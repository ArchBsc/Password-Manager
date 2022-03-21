## Password Manager

import re, os, csv
from getpass import getpass

## First part 

print("1. New user \n2. Login ")

before_login = int(input("Select a number (from 1 to 2): "))

class cmain():
    
    def __init__(self, username, email, password, rep_password):
        
        self.username = username
        self.password = password 
        self.rep_password = rep_password
        self.email = email
    
    def regit(self, username, email, password): 

        with open("data.txt", "a") as file:
            file.write("\n"+username+","+email+","+password)
    
    def login(self):

        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = getpass("Enter your master password: ")
        rep_password = getpass("Repeat your master password: ")



    def password_verification(self, password, rep_password):
        if (self.password == self.rep_password):
            pass 
        else:
            print("The master password is not the same with repeat password")
                

def main():

    if before_login == 1:

        ## User input 
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        master_password = getpass("Enter your master password: ")
        rep_password = getpass("Repeat your master password: ")
        user = cmain(username, email, master_password, rep_password)
    
        ## Data verification 
        user.password_verification(master_password, rep_password)
        
        ## Store data
        user.regit(username, email, master_password)

if __name__ == '__main__':
    main()
