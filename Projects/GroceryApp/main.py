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
def add_groceries(category, g_item, amount):    #POST
    #Need to add api interaction with website for categories
    connect = sqlite3.connect("grocerylist.db")
    cursor = connect.cursor()
    if category == 'Food':
        cursor.execute("INSERT INTO Food (food, amount) VALUES (?, ?)", (g_item, amount))
    elif category == 'Nonfood':
        cursor.execute("INSERT INTO Nonfood (item, amount) VALUES (?, ?)", (g_item, amount))
    
    connect.commit()
    connect.close()

def edit_groceries(category, new_g_item, new_amount, current_g_item):   #PUT
    #Need to add api interaction with website for categories
    connect = sqlite3.connect("grocerylist.db")
    cursor = connect.cursor()
    if category == 'Food':
        cursor.execute("UPDATE Food SET food = ?, amound = ?,  WHERE food = ?", (new_g_item, new_amount, current_g_item))
    elif category == 'Nonfood':
        cursor.execute("UPDATE Nonfood SET item = ?, amount = ?, WHERE item = ?", (new_g_item, new_amount, current_g_item))
    
    connect.commit()
    connect.close()    

def remove_groceries(category, g_item):
    connect = sqlite3.connect("grocerylist.db")
    cursor = connect.cursor()
    if category == 'Food':
        cursor.execute("DELETE FROM Food WHERE food = ?", (g_item,))
    elif category == 'Nonfood':
        cursor.execute("DELETE FROM Nonfood WHERE item = ?", (g_item,))
    
    connect.commit()
    connect.close()  







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