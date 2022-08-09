import sqlite3, hashlib, re
from datetime import date
from datetime import datetime
from getpass import getpass
from cryptography.fernet import Fernet

def new_item():


    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    item_number = int(input("How many items do you want to create \n: "))

    count = 1
        
    c.execute("""CREATE TABLE IF NOT EXISTS item(
            username text,
            email text,
            passwd text,
            website text
    )""")   

    
    
    while count <= int(item_number):
        
        a = str(input("Enter your username: "))
        b = str(input("Enter your email: "))
        h = str(getpass("Enter your password: "))
        z = str(input("Enter the url of website: "))

        c.execute("INSERT INTO item VALUES(?,?,?,?)", (a, b, h, z))
        
        count += 1
        conn.commit()


    conn.commit()
    conn.close()


        
def item_search(pattern):


    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    
    c.execute("SELECT * FROM item")

    items = c.fetchall()
    number = 1
    for item in items:

        lusername = str(item[0])
        lemail = str(item[1])
        lpassword = str(item[2])
        lurl = str(item[3])

    
        if re.search(pattern, lusername):
            print("Username: "+lusername+ ", Email: "+ lemail+ ", Password: " + lpassword+ ", Url: "+ lurl)
        else:
            pass
        

    conn.commit()
    conn.close()
    



def Encrypt():
    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM cr")
    info = c.fetchall()
    
    for item in info:
            username = str(item[0])
            password = str(item[1])
            
    key = password
    
    with open("database.db", "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    
    with open("database.db", "wb") as f:
        f.write(encrypted)

    conn.commit()
    conn.close()

def Dencrypt(password):
    
    paswd = hashlib.sha256(str.encode(password)).hexdigest()
    key = "b'" + str(paswd[0:42]) + "='"
    
    with open("database.db", "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    dencrypted = fernet.decrypt(data)
    
    with open("database.db", "wb") as f:
        f.write(dencrypted)     


