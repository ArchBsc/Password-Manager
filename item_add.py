import sqlite3, hashlib, re, random
from getpass import getpass
from cryptography.fernet import Fernet
from rich import print
from tabulate import tabulate

def new_item():


    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    print("[#14BDFF]How many items do you want to create[/#14BDFF]")
    item_number = int(input(": "))

    count = 1
    
    try:
        c.execute("SELECT * FROM item")
        items = c.fetchall()

        for item in items:
            lid = str(item[0])
            lusername = str(item[1])
            lemail = str(item[2])
            lpassword = str(item[3])
            lurl = str(item[4])
            
                
    except sqlite3.OperationalError:
        c.execute("""CREATE TABLE IF NOT EXISTS item(
            id number,
            username text,
            email text,
            passwd text,
            website text
        )""")
        id = 0
        lid = str(id)
        test = "test"
        c.execute("INSERT INTO item VALUES(?,?,?,?,?)", (lid,test,test,test,test))
    

    while count <= int(item_number):
        id = str(int(lid) + 1) 
        print(id)
        print("[#14BDFF]Enter your username; [/#14BDFF]")
        a = str(input())
        print("[#14BDFF]Enter your email: [/#14BDFF]")
        b = str(input())
        print("[#14BDFF]Enter your password: [/#14BDFF]")
        h = str(getpass())
        print("[#14BDFF]Enter the url of website: [/#14BDFF]")
        z = str(input())

        c.execute("INSERT INTO item VALUES(?,?,?,?,?)", (id, a, b, h, z))
        
        count += 1
        conn.commit()

    
    conn.commit()
    conn.close()

def password_gen():

    pass_len = input("How long do you want password to be; \n")
    pass_num = input("How many numbers do you want the password to have? \n")
    pass_syn = input("How many special characters do you want the password to have? \n")

    syn = "!@#$%^&*()_+-=:'<>?/.,"
    num = "1234567890"
    low_let = "qwertyuioplkjhgfdsazxcvbnm"
    upper_let =  low_let.upper()

    all = ""
    if pass_num != 0:
        all += num
    if pass_syn != 0:
        all += syn
    all += low_let
    all += upper_let

    for x in range(1):
        password = "".join(random.sample(all, pass_len))
    print(password)

def item_search(pattern):

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    
    c.execute("SELECT * FROM item")
    if pattern == "all":
        items = c.fetchall()
        number = 1
        table_date = [["[#0E7C83]id[/#0E7C83]", "[#14BDFF]Username[/#14BDFF]", "[#14BDFF]Email[/#14BDFF]", "[#14BDFF]Password[/#14BDFF]", "[#14BDFF]Url[/#14BDFF]"]]
        for item in items:
            lid = str(item[0])
            lusername = str(item[1])
            lemail = str(item[2])
            lpassword = str(item[3])
            lurl = str(item[4])
            let = ["[#0E7C83]"+ str(number) + "[/#0E7C83]", "[#12FFA4]"+ str(lusername) +"[/#12FFA4]", "[#12FFA4]"+ str(lemail) +"[/#12FFA4]", "[#12FFA4]"+ str(lpassword) +"[/#12FFA4]", "[#12FFA4]"+ str(lurl) +"[/#12FFA4]"]
            number += 1
            table_date.append(let)
        print(tabulate(table_date, tablefmt="plain"))
    else:    
        items = c.fetchall()
        number = 1
        table_date = [["[#14BDFF]Username[/#14BDFF]", "[#14BDFF]Email[/#14BDFF]", "[#14BDFF]Password[/#14BDFF]", "[#14BDFF]Url[/#14BDFF]"]]

        for item in items:

            lid = str(item[0])
            lusername = str(item[1])
            lemail = str(item[2])
            lpassword = str(item[3])
            lurl = str(item[4])

        
            if re.search(pattern, lusername):
                let = ["[#12FFA4]"+ str(lusername) +"[/#12FFA4]", "[#12FFA4]"+ str(lemail) +"[/#12FFA4]", "[#12FFA4]"+ str(lpassword) +"[/#12FFA4]", "[#12FFA4]"+ str(lurl) +"[/#12FFA4]"]
                table_date.append(let)
            else: 
                break
        print(tabulate(table_date, tablefmt="plain"))
          

        conn.commit()
        conn.close()
        
def delete():

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM item")

    items = c.fetchall()
    number = 1
    table_date = [["[#0E7C83]id[/#0E7C83]", "[#14BDFF]Username[/#14BDFF]", "[#14BDFF]Email[/#14BDFF]", "[#14BDFF]Password[/#14BDFF]", "[#14BDFF]Url[/#14BDFF]"]]
    for item in items:
        lid = str(item[0])
        lusername = str(item[1])
        lemail = str(item[2])
        lpassword = str(item[3])
        lurl = str(item[4])
        let = ["[#0E7C83]"+ str(number) + "[/#0E7C83]", "[#12FFA4]"+ str(lusername) +"[/#12FFA4]", "[#12FFA4]"+ str(lemail) +"[/#12FFA4]", "[#12FFA4]"+ str(lpassword) +"[/#12FFA4]", "[#12FFA4]"+ str(lurl) +"[/#12FFA4]"]
        number += 1
        table_date.append(let)
    print(tabulate(table_date, tablefmt="plain"))

    row = int(input("What is the item number? \n:"))
    
    c.execute("DELETE from item WHERE id=(?)", (str(row)))
    

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

