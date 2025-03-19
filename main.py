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

###### Functions ######
def login():
    """Check if username and password are corrects
    """
    pass

def register():
    """ Create a profile (Username + password)
    """

def menu():
    selection = int(input("""
    1) Add an item.
    2) Remove an item
    3) Read an item.
    4) Edit an item.
    5) Check if passwords and email addresses are in a data breach.
    
    Press Enter to exit
    """))

    if selection ==1:
        add()
        return menu()
    elif selection ==2:
        remove()
        return menu()
    elif selection ==3:
        read()
        return menu()
    elif selection ==4:
        edit()
        return menu()
    elif selection == 5:
        check()
        return menu()
    else:
        menu()


def startup():
    """ Ask if the user has an account.
    """
    answer = input("Do you have a master password ? (Y/N)")
    
    if answer == "Y":
        return login()
    elif answer =="N":
        return register()
    else: 
        print("Please, return Y or N.")
        startup()

def add():
    pass

def remove():
    pass

def check():
    pass

def remove():
    pass

def read():
    pass

####### Code #######

#Sartup
startup()

#Create a database
db = sqlite3.connect("psdmng.db")
#Set a cursor
cursor = db.cursor()
#If the print works, the connection is established
print("DB is connected")

#Check if a table exists.
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
check1 = cursor.fetchone()
if not check1: #Empty list
    sql_command1 = """CREATE TABLE IF NOT EXISTS logins (id INTEGER PRIMARY KEY, platform TEXT NOT NULL UNIQUE, usernames TEXT, email TEXT,passwords TEXT NOT NULL ) """
    cursor.execute(sql_command1)
 
menu()




#Close th db 
db.close()


