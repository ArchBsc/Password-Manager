import sqlite3, hashlib, re
from getpass import getpass

def new_acc(name, password):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS cr(
                name text,
                password text
        )""")   
        
        password_hash = hashlib.sha256(str.encode(password)).hexdigest()
        passwd = "b'" + str(password_hash[0:42]) + "='"

        c.execute("INSERT INTO cr VALUES(?,?)", (name, passwd))

        conn.commit()
        conn.close()

def login(lname, lpassword):

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT * FROM cr")
        info = c.fetchall()
        
        for item in info:
                username = str(item[0])
                password = str(item[1])
        
        login_password_hash = hashlib.sha256(str.encode(lpassword)).hexdigest()
        login_passwd = "b'" + str(login_password_hash[0:42]) + "='"

        if (login_passwd == password) & (lname == username):
                pass
        else:
                print(":(")
                return login(input("Enter your name: "), getpass("Enter your password: "))

        conn.commit()
        conn.close()
