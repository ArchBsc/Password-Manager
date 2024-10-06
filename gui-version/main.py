import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3, hashlib, os


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Frame Switcher")
        self.root.geometry("400x600")

        self.frame1 = Frame1(self.root, self)  
        self.frame2 = Frame2(self.root, self)  
        self.frame3 = Frame3(self.root, self)
        self.frame4 = Frame4(self.root, self)
        self.frame5 = Frame5(self.root, self)
        self.frame6 = Frame6(self.root, self)

        self.show_frame1()  

    def show_frame1(self):
        self.frame2.hide()  
        self.frame1.show() 
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame6.hide()

    def show_frame2(self):
        self.frame1.hide() 
        self.frame2.show()  
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame6.hide()

    def show_frame3(self):
        self.frame1.hide()  
        self.frame2.hide()  
        self.frame3.show()
        self.frame4.hide()
        self.frame5.hide()
        self.frame6.hide()    

    def show_frame4(self):
        self.frame1.hide()  
        self.frame2.hide()  
        self.frame3.hide()
        self.frame4.show()
        self.frame5.hide()
        self.frame6.hide()

    def show_frame5(self):
        self.frame1.hide()  
        self.frame2.hide()  
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.show()
        self.frame6.hide()

    
    def show_frame6(self, iname=None):
        self.frame1.hide()  
        self.frame2.hide()  
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame6.show(iname)
        
    
class Frame1:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        
        tk.Label(self.frame, text="Welcome").pack(pady=10)
        tk.Button(self.frame, text="Log in", command=self.app.show_frame2).place(relx=.5,rely=0.2, anchor="center", relwidth=0.7, relheight=0.1)
        tk.Button(self.frame, text="Sign in", command=self.app.show_frame3).place(relx=.5,rely=0.3, anchor="center", relwidth=0.7, relheight=0.1)
        
    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()

class Frame2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        
        tk.Label(self.frame, text="Log in").pack(pady=10)
        
        self.usr = tk.Entry(self.frame)
        self.usr.pack(pady=2)
        self.set_placeholder(self.usr, "Enter your username or email")
        
        self.passwor = tk.Entry(self.frame, show="*")
        self.passwor.pack(pady=2)
        self.set_placeholder(self.passwor, "Enter your password")

        tk.Button(self.frame, text="Enter", command=self.new_acc).pack(pady=10)
        tk.Button(self.frame, text="Back", command=self.app.show_frame1).pack()

    def set_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.config(fg='grey')
        entry.bind("<FocusIn>", lambda event, e=entry, ph=placeholder: self.clear_placeholder(event, e, ph))
        entry.bind("<FocusOut>", lambda event, e=entry, ph=placeholder: self.add_placeholder(event, e, ph))

    def clear_placeholder(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black', show="*" if entry == self.passwor else '')

    def add_placeholder(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='grey', show="" if entry == self.passwor else '')

    def new_acc(self):
        name = self.usr.get()
        password = self.passwor.get()

        if not name or not password or \
           name == "Enter your username or email" or password == "Enter your password":
            print("Username and password cannot be empty.")
            return

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        c.execute("INSERT INTO cr VALUES(?,?)", (name, password_hash))
        conn.commit()
        conn.close()
        
        self.app.show_frame4()

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()


class Frame3:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        tk.Label(self.frame, text="Sign in").pack(pady=10)
        
        self.usr = tk.Entry(self.frame)
        self.usr.pack(pady=2)
        self.set_placeholder(self.usr, "Enter your username or email")

        self.passwor = tk.Entry(self.frame, show="*")
        self.passwor.pack(pady=2)
        self.set_placeholder(self.passwor, "Enter your password")

        tk.Button(self.frame, text="Enter", command=self.login).pack(pady=10)
        tk.Button(self.frame, text="Back", command=self.app.show_frame1).pack()

    def set_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.config(fg='grey')
        entry.bind("<FocusIn>", lambda event, e=entry, ph=placeholder: self.clear_placeholder(event, e, ph))
        entry.bind("<FocusOut>", lambda event, e=entry, ph=placeholder: self.add_placeholder(event, e, ph))

    def clear_placeholder(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black', show="*" if entry == self.passwor else '')

    def add_placeholder(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='grey', show="" if entry == self.passwor else '')

    def login(self):
        lname = self.usr.get()
        lpassword = self.passwor.get()

        if not lname or not lpassword or \
           lname == "Enter your username or email" or lpassword == "Enter your password":
            print("Username and password cannot be empty.")
            return

        try:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()

            c.execute("SELECT * FROM cr WHERE name=?", (lname,))
            user_data = c.fetchone()

            if user_data is None:
                print("Username not found.")
                return

            stored_username, stored_password_hash = user_data
            login_password_hash = hashlib.sha256(lpassword.encode()).hexdigest()

            if login_password_hash == stored_password_hash:
                print("Login successful!")
                self.app.show_frame4()
            else:
                print("Invalid password.")
        except Exception as e:
            print(f"Error during login: {e}")
        finally:
            conn.close()

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()


class Frame4:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.add_button = tk.Button(self.frame, text="+", command=self.app.show_frame5, height=2)
        self.add_button.pack(fill='x', padx=0, pady=0)

        self.canvas = tk.Canvas(self.frame)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def item(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM item")
        items = c.fetchall()
        conn.close()

        if not items:
            empty_label = tk.Label(self.scrollable_frame, text="No items found.")
            empty_label.pack(pady=10) 
            return

        for item in items:
            iname = str(item[0])

            item_button = tk.Button(
                self.scrollable_frame,
                text=iname,
                command=lambda iname=iname: self.app.show_frame6(iname),
                height=2
            )
            item_button.pack(fill='x', padx=5, pady=2)  

            delete_button = tk.Button(
                self.scrollable_frame,
                text="Delete",
                command=lambda iname=iname: self.delete_item(iname),
                height=2
            )
            delete_button.pack(fill='x', padx=5, pady=2) 

    def delete_item(self, item_name):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("DELETE FROM item WHERE iname=?", (item_name,))
        conn.commit()
        conn.close()

        self.item()

    def show(self):
        self.item()  
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()



class Frame5:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        tk.Label(self.frame, text="New item").pack(pady=10)

        self.iname = tk.Entry(self.frame)
        self.iname.pack(pady=2)
        self.set_placeholder(self.iname, "Enter item name")

        self.web = tk.Entry(self.frame)
        self.web.pack(pady=2)
        self.set_placeholder(self.web, "Enter website URL")

        self.passwor = tk.Entry(self.frame, show="*")
        self.passwor.pack(pady=2)
        self.set_placeholder(self.passwor, "Enter password")

        self.email = tk.Entry(self.frame)
        self.email.pack(pady=2)
        self.set_placeholder(self.email, "Enter email address")

        tk.Button(self.frame, text="Enter", command=self.item_add).pack()
        tk.Button(self.frame, text="Back", command=self.app.show_frame4).pack()

    def set_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.config(fg='grey')
        entry.bind("<FocusIn>", lambda event, e=entry, ph=placeholder: self.clear_placeholder(event, e, ph))
        entry.bind("<FocusOut>", lambda event, e=entry, ph=placeholder: self.add_placeholder(event, e, ph))

    def clear_placeholder(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black', show="*" if entry == self.passwor else '')

    def add_placeholder(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='grey', show="" if entry == self.passwor else '')

    def item_add(self):
        item_name = self.iname.get()            
        email = self.email.get()    
        password = self.passwor.get()  
        web = self.web.get()

        if not web or not password or not item_name or not email or \
           item_name == "Enter item name" or email == "Enter email address" or \
           password == "Enter password" or web == "Enter website URL":
            print("All fields are required.")
            return

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO item VALUES (?, ?, ?, ?)", (item_name, email, password, web))
        conn.commit()
        conn.close()
        self.clear_entries()
        
        self.app.show_frame4()

    def clear_entries(self):
        self.iname.delete(0, tk.END)
        self.web.delete(0, tk.END)
        self.passwor.delete(0, tk.END)
        self.email.delete(0, tk.END)
        
        self.set_placeholder(self.iname, "Enter item name")
        self.set_placeholder(self.web, "Enter website URL")
        self.set_placeholder(self.passwor, "Enter password")
        self.set_placeholder(self.email, "Enter email address")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()


class Frame6:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

    def view_item(self, iname):
        for widget in self.frame.winfo_children():
            widget.destroy() 

        tk.Label(self.frame, text="View Item").pack(pady=10)

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE iname=?", (iname,))
        item = c.fetchone()
        conn.close()

        if item:
            tk.Label(self.frame, text=f"Name: {item[0]}").pack(pady=10)
            tk.Label(self.frame, text=f"Email: {item[1]}").pack(pady=10)
            tk.Label(self.frame, text=f"Password: {item[2]}").pack(pady=10)
            tk.Label(self.frame, text=f"Website: {item[3]}").pack(pady=10)
            tk.Button(self.frame, text="back", command=self.app .show_frame4).place(relx=.06, rely=0.06, anchor="center", relwidth=0.1, relheight=0.1)
        else:
            tk.Label(self.frame, text="Item not found.").pack(pady=10)

    def show(self, iname=None):
        self.view_item(iname)
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()


def initialize_database():
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS cr(
                name text,
                password text
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS item(
                iname TEXT,
                email TEXT,
                passwd TEXT,
                website TEXT
            )""")
        conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    if not os.path.exists("database.db"):
        initialize_database()

    try:
        root = tk.Tk()
        app = App(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")