import sqlite3, hashlib, re 
from datetime import date
from datetime import datetime
from getpass import getpass


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

def repit(filename1, filename2):

        item_quest = input("1)New item \n2)View items \n3)Exit \n:")
        
        if item_quest == 1:
            filename1.new_item(str(input("Enter your username: ")), str(input("Enter your email: ")), str(getpass("Enter your password: ")), str(input("Enter the url of website: ")))
            
            quest_2 = input("1)New item \n2)View items \n3)Exit \n: ") 

            if int(quest_2) == 1:
                filename2.new_item(str(input("What is the name of the item; \n: ")))
                repit(filename1, filename2)
            elif int(quest_2) == 2:
                filename2.item_search(str(input("What is the name of the item; \n: ")))
                repit(filename1, filename2)
            else:
                pass

        else:
            pass