from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3
#def main():
    
connect = sqlite3.connect("grocerylist.db")
cursor = connect.cursor()
cursor.execute("SELECT * FROM grocerylist.")  # Query all rows from the grocerylist table
rows = cursor.fetchall()
print(rows)

#tables = open("/grocerylist.db")
#print(tables)




    
    
    
#    if __name__ == "__main__":
#       main()  # Run the server when the script is executed