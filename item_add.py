import sqlite3, hashlib, re, random, string
from getpass import getpass
from cryptography.fernet import Fernet
from rich import print
from tabulate import tabulate
from datetime import date
from datetime import datetime

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
        c.execute("SELECT * FROM item")
        items = c.fetchall()

        for item in items:
            lid = str(item[0])
            lusername = str(item[1])
            lemail = str(item[2])
            lpassword = str(item[3])
            lurl = str(item[4])

        if item_number == 1:
            id = str(int(lid) + 1)
            print("[#14BDFF]Enter your username; [/#14BDFF]")
            a = str(input())
            print("[#14BDFF]Enter your email: [/#14BDFF]")
            b = str(input())
            print("[#14BDFF]Do you want to generate the password[/#14BDFF] (type yes to generate);")
            pass_gen = input(": ")
            if pass_gen == "yes":
                h = str(password_gen())
            else:
                print("[#14BDFF]Enter your password[#FFFFFF]:[/#FFFFFF] [/#14BDFF]")
                h = str(getpass())
            print("[#14BDFF]Enter the url of website: [/#14BDFF]")
            z = str(input())

        else:
            id = str(int(lid) + 1)
            print("[#14BDFF]Enter your username; [/#14BDFF]")
            a = str(input())
            print("[#14BDFF]Enter your email: [/#14BDFF]")
            b = str(input())
            print("[#14BDFF]Do you want to generate the password[/#14BDFF] (type yes to generate);")
            pass_gen = input(": ")
            if pass_gen == "yes":
                h = str(password_gen())
            else:
                print("[#14BDFF]Enter your password[#FFFFFF]:[/#FFFFFF] [/#14BDFF]")
                h = str(getpass())
            print("[#14BDFF]Enter the url of website[#FFFFFF]:[/#FFFFFF] [/#14BDFF]")
            z = str(input())
            print("\n[underline][#12FFA4]                         [/#12FFA4][/underline]")
        

        c.execute("INSERT INTO item VALUES(?,?,?,?,?)", (id, a, b, h, z))
        
        count += 1
        conn.commit()

    
    conn.commit()
    conn.close()

def password_gen():
    print("[#12FFA4]How long do you want password to be[/#12FFA4];")
    pass_len = int(input(": "))
    print("[#12FFA4]Do you want to have numbers (type yes to add numbers)[/#12FFA4];")
    pass_num = input(": ")
    print("[#12FFA4]Do you want to have syntax (type yes to add numbers)[/#12FFA4];")
    pass_syn = input(": ")

    syn = "!@#$%^&*()_+-=:'<>?/.,"
    num = "1234567890"
    low_let = "qwertyuioplkjhgfdsazxcvbnm"
    upper_let =  low_let.upper()

    all = []
    if pass_num == "yes":
        all.extend(num)
    if pass_syn == "yes":    
        all.extend(syn)
    all.extend(low_let)
    all.extend(upper_let)

    random.shuffle(all)

    password = "".join(all[0:pass_len])
    
    return password

def safe_note():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    print("[#14BDFF]How many notes do you want to create[/#14BDFF]")
    note_number = int(input(": "))

    count = 1
    
    try:
        c.execute("SELECT * FROM notes")
        notes = c.fetchall()

        for note in notes:
            lid = str(note[0])
            lnotes = str(note[1])
            ltime = str(note[2])
            lname = str(note[3])
                
    except sqlite3.OperationalError:
        c.execute("""CREATE TABLE IF NOT EXISTS notes(
            id number,
            note text,
            time text,
            name text
        )""")
        id = 0
        lid = str(id)
        test = "test"
        c.execute("INSERT INTO notes VALUES(?,?,?,?)", (lid,test,test,test))

    
    while count <= int(note_number):
        c.execute("SELECT * FROM notes")
        notes = c.fetchall()

        for note in notes:
            lid = str(note[0])
            lnotes = str(note[1])
            ltime = str(note[2])
            lname = str(note[3])

        if note_number == 1:
            id = str(int(lid) + 1)

            print("[#14BDFF]Enter your username; [/#14BDFF]")
            name = input(":")

            print("[#14BDFF]Note: [/#14BDFF]")
            note = input("")

            now = datetime.now()
            curr_date = ("["+str(date.today())+"]")
            time = str(now.strftime("%H:%M"))
            today = curr_date +"-"+ time

        else:
            id = str(int(lid) + 1)

            print("[#14BDFF]Enter your username; [/#14BDFF]")
            name = input(": ")
            
            print("[#14BDFF]Note: [/#14BDFF]")
            note = input("")
            
            now = datetime.now()
            curr_date = ("["+str(date.today())+"]")
            time = str(now.strftime("%H:%M"))
            today = curr_date +"-"+ time

        c.execute("INSERT INTO notes VALUES(?,?,?,?)", (id, note, today, name))
        
        count += 1
        conn.commit()

    
    conn.commit()
    conn.close()

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

def safe_note_search(pattern):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    
    c.execute("SELECT * FROM notes")
    if pattern == "all":
        notes = c.fetchall()
        for note in notes:
            lid = str(note[0])
            lnotes = str(note[1])
            ltime = str(note[2])
            lname = str(note[3])

            print("[#0E7C83]"+ltime + "[/#0E7C83]" + "   " + "[#12FFA4]" +lnotes + "[/#12FFA4]")


    else:    
        notes = c.fetchall()
        for note in notes:
            lid = str(note[0])
            lnotes = str(note[1])
            ltime = str(note[2])
            lname = str(note[3])
            
            if re.search(pattern, lname):
                print("[#0E7C83]"+ltime + "[/#0E7C83]" + "   " + "[#12FFA4]" +lnotes + "[/#12FFA4]")
            else: 
                break

        conn.commit()
        conn.close()

def delete_item():

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
        let = ["[#0E7C83]"+ str(lid) + "[/#0E7C83]", "[#12FFA4]"+ str(lusername) +"[/#12FFA4]", "[#12FFA4]"+ str(lemail) +"[/#12FFA4]", "[#12FFA4]"+ str(lpassword) +"[/#12FFA4]", "[#12FFA4]"+ str(lurl) +"[/#12FFA4]"]
        number += 1
        table_date.append(let)
    print(tabulate(table_date, tablefmt="plain"))

    row = str(input("What is the item number? \n:"))
    
    c.execute("DELETE from item WHERE id=(?)", (row))


    conn.commit()
    conn.close()

def delete_note():
    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM notes")

    
    notes = c.fetchall()
    for note in notes:
        lid = str(note[0])
        lnotes = str(note[1])
        ltime = str(note[2])
        lname = str(note[3])

        print("[#0E7C83]"+ lid +")[/#0E7C83] "+"[#0E7C83]"+ltime + "[/#0E7C83]" + "   " + "[#12FFA4]" +lnotes + "[/#12FFA4]")

    row = str(input("What is the note number? \n:"))
    
    c.execute("DELETE from notes WHERE id=(?)", (row))


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

