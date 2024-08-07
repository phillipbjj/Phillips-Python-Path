from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3
#def main():
    
connect = sqlite3.connect("grocerylist.db")
cursor = connect.cursor()

"""#Created the 2 tables I am using.
#cursor.execute("CREATE TABLE Food(food TEXT, amount TEXT)")    
#cursor.execute("CREATE TABLE Nonfood(item TEXT, amount TEXT)")
#connect.close() #Closes the database connection.
#connect.commit() #This saves the changes to my database."""

cursor.execute("SELECT * FROM grocerylist.")  # Query all rows from the grocerylist table
rows = cursor.fetchall()

#Add groceries into one of the 2 categories(tables)
def add_groceries(category, g_item, amount):
    #Need to add api interaction with website for categories
    connect = sqlite3.connect("grocerylist.db")
    cursor = connect.cursor()
    if category == 'Food':
        cursor.execute("INSERT INTO Food (food, amount) VALUES (?, ?)", (g_item, amount))
    elif category == 'Nonfood':
        cursor.execute("INSERT INTO Nonfood (item, amount) VALUES (?, ?)", (g_item, amount))
    else:
        raise ValueError("Invalid category. Must be 'Food' or 'Nonfood'.")
    connect.commit()
    connect.close()
    
    """ # Connect to SQLite3 database and insert the new item
            conn = sqlite3.connect('grocerylist.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO grocerylist (item, quantity) VALUES (?, ?)", (item, quantity))
            conn.commit()  # Commit the changes to the database
            conn.close()  # Close the database connection"""


def get_grocery_list(self):
        # Connect to SQLite3 database and retrieve the grocery list
        connect = sqlite3.connect('grocerylist.db')
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM grocerylist")  # Query all rows from the grocerylist table
        rows = cursor.fetchall()  # Fetch all rows from the query result
        connect.close()  # Close the database connection

#tables = open("/grocerylist.db")
#print(tables)




    
    
    
#    if __name__ == "__main__":
#       main()  # Run the server when the script is executed