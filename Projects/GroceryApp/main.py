from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

def main():
    
    connect = sqlite3.connect("grocerylist.db")
    cursor = connect.cursor()
    #ADD LAST PRICE FOR AFTER PURCHASE OF GROCERIES, CAN BE TURNED INTO A REPRESENTATION MODEL LATER
    """#Created the 2 tables I am using.
    #cursor.execute("CREATE TABLE Food(food TEXT, amount TEXT)")    
    #cursor.execute("CREATE TABLE Nonfood(item TEXT, amount TEXT)")
    #connect.close() #Closes the database connection.
    #connect.commit() #This saves the changes to my database.
    cursor.execute("SELECT * FROM grocerylist.")  # Query all rows from the grocerylist table
    rows = cursor.fetchall()"""
    #Inherits pythons HTTP handler as a subclass for HTTP operations
    class GroceryHandler(BaseHTTPRequestHandler):
        
        def _set_response(self, status=200):  # Default status is 200 (OK)
            self.send_response(status)  # Sends the HTTP status code
            self.send_header('Content-type', 'application/json')  # Specifies that the content is JSON
            self.end_headers()  # Ends the headers section, ready to send content
        
        # Handling the GET request to view the webpage and database contents
        def do_GET(self):
            self.path == '/':  # Check if the root path is requested
            # Open and read the index.html file
            with open('index.html', 'rb') as file:
                self.send_response(200) #Send a 200 OK response
                self.send_header('Content-type', 'text/html')
                self.end_headers() # End the headers
                self.wfile.write(file.read())
            
                connect = sqlite3.connect("grocerylist.db")
                cursor = connect.cursor()

                # Fetching data from both Food and Nonfood tables
                cursor.execute("SELECT food, amount FROM Food")
                food_data = cursor.fetchall()
                cursor.execute("SELECT item, amount FROM Nonfood")
                nonfood_data = cursor.fetchall()

                connect.close()

                # Formatting the data as a JSON response
                response_data = {
                    'Food': [{'food': item[0], 'amount': item[1]} for item in food_data],
                    'Nonfood': [{'item': item[0], 'amount': item[1]} for item in nonfood_data]
                }

                self._set_response()  # Set the response status and headers
                self.wfile.write(json.dumps(response_data).encode('utf-8'))  # Send the JSON data
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
        #Update current groceries list groceries
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
        #Remove groceries from the list
        def remove_groceries(category, g_item):
            connect = sqlite3.connect("grocerylist.db")
            cursor = connect.cursor()
            if category == 'Food':
                cursor.execute("DELETE FROM Food WHERE food = ?", (g_item,))
            elif category == 'Nonfood':
                cursor.execute("DELETE FROM Nonfood WHERE item = ?", (g_item,))
            
            connect.commit()
            connect.close()  

        """def get_grocery_list(self):
                # Connect to SQLite3 database and retrieve the grocery list
                connect = sqlite3.connect('grocerylist.db')
                cursor = connect.cursor()
                cursor.execute("SELECT * FROM grocerylist")  # Query all rows from the grocerylist table
                rows = cursor.fetchall()  # Fetch all rows from the query result
                connect.close()  # Close the database connection"""





    
    
    
if __name__ == "__main__":
    main()  # Run the server when the script is executed