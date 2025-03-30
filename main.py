#!/usr/bin/env python

print("""
██████╗ ███████╗██████╗ ███╗   ███╗███╗   ██╗ ██████╗ 
██╔══██╗██╔════╝██╔══██╗████╗ ████║████╗  ██║██╔════╝ 
██████╔╝███████╗██║  ██║██╔████╔██║██╔██╗ ██║██║  ███╗
██╔═══╝ ╚════██║██║  ██║██║╚██╔╝██║██║╚██╗██║██║   ██║
██║     ███████║██████╔╝██║ ╚═╝ ██║██║ ╚████║╚██████╔╝
╚═╝     ╚══════╝╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                      
""")
#db = database

###### Libraries ######
import sqlite3
from psdgen import psdgen

###### Functions ######
def login():
    """Check if username and password are corrects
    """
    pass

def register():
    """ Create a profile (Username + password)
    """

def menu():
    selection = input("""
    1) Add an item.
    2) Remove an item
    3) Read an item.
    4) Edit an item.
    5) Check if passwords and email addresses are in a data breach.
    
    Press Enter to exit
    """)

    if selection =="1":
        add()
        return menu()
    elif selection =="2":
        remove()
        return menu()
    elif selection =="3":
        read()
        return menu()
    elif selection =="4":
        edit()
        return menu()
    elif selection == "5":
        check()
        return menu()


def startup():
    """ Ask if the user has an account.
    """
    answer = input("Do you have a master password ? (Y/N)")
    
    if answer == "Y" or answer =="y":
        return login()
    elif answer =="N" or answer =="n":
        return register()
    else: 
        print("Please, return Y or N.")
        startup()

def add():
    choice = input("Do you want to manually set your password ? If not, it will automatically be generated (Y/N)")
    
    if choice =="Y" or choice =="y":
        platform = input("Platform name :")
        email = input("Email adress :")
        username = input("Username :")
        password = input("Password :")
    
    elif choice == "N" or choice =="n":
        platform = input("Platform name :")
        email = input("Email adress :")
        username = input("Username :")
        lenght =  int(input("Password lenght ?"))
        password = psdgen(lenght)
    else:
        print("Please, return Y or N.")
        add()

    valid = input(f"Are {platform}, {email} {username}, {password} correct?(Y/N)")
    if valid =="Y" or valid =="y":
        sql_command_add = """INSERT INTO logins(platform,email,usernames,passwords) VALUES(?,?,?,?)"""
        cursor.execute(sql_command_add,(platform,email,username,password))
        db.commit()
        print("\033[92m[✓] Item added\033[00m")

    elif valid == "N" or valid =="n":
        return add()
    

def remove():
    L = """SELECT platform FROM logins"""
    cursor.execute(L)
    platforms = cursor.fetchall()
    print(platforms,"Select the platform you want to delete.")

    platform = input("Wich one do you want to delete ?")
    sql_command_rm = "DELETE FROM logins where platform = ?"
    cursor.execute(sql_command_rm,(platform,))
    db.commit()
    print(f"\033[92m[✓] {platform} has been deleted.\033[00m")

def check():
    pass


def read():
    L = """SELECT platform FROM logins"""
    cursor.execute(L)
    platforms = cursor.fetchall()
    print(platforms)
    
    platform = input("Which platform do you want to see? ")
    sql_command_read = "SELECT platform, usernames, email,passwords FROM logins WHERE platform =?"
    cursor.execute(sql_command_read,(platform,))
    val = cursor.fetchall()
    
    if val:
        print(val)
    else:
        print("\033[91m [✗]No data found for this platform.\033[00m")
    
    return val

####### Code #######

#Sartup
startup()

#Create a database
db = sqlite3.connect("psdmng.db")
#Set a cursor
cursor = db.cursor()
#If the print works, the connection is established
print("\033[92m[✓]DB is connected \033[00m")

#Check if a table exists.
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
check1 = cursor.fetchone()
if not check1: #Empty list
    sql_command1 = """CREATE TABLE IF NOT EXISTS logins (id INTEGER PRIMARY KEY, platform TEXT NOT NULL UNIQUE, usernames TEXT, email TEXT,passwords TEXT NOT NULL ) """
    cursor.execute(sql_command1)
 
menu()




#Close th db 
db.close()


