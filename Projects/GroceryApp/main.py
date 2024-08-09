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
        
        #Handling the GET request to view the webpage and database contents
        def do_GET(self):
            #Open and read the index.html file
            with open('index.html', 'rb') as file:
                self.send_response(200) #Send a 200 OK response
                self.send_header('Content-type', 'text/html') #Set the content type to HTML
                self.end_headers() # End the headers
                self.wfile.write(file.read()) #Write the content of the file to the response
        """def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Gets the size of the incoming data
        post_data = self.rfile.read(content_length)  # Reads the incoming data based on its length
        data = json.loads(post_data)  # Decodes the JSON data into a Python dictionary

        # Extracting data from the JSON payload
        category = data['category']
        g_item = data['g_item']
        amount = data['amount']
        
        # Connecting to the SQLite database
        connect = sqlite3.connect("grocerylist.db")
        cursor = connect.cursor()  # Creating a cursor object to execute SQL commands
        
        # Inserting the data into the appropriate table based on the category
        if category == 'Food':
            cursor.execute("INSERT INTO Food (food, amount) VALUES (?, ?)", (g_item, amount))
        elif category == 'Nonfood':
            cursor.execute("INSERT INTO Nonfood (item, amount) VALUES (?, ?)", (g_item, amount))
        
        # Committing the transaction and closing the connection
        connect.commit()
        connect.close()
        
        # Sending a response back to the client
        self._set_response(201)  # 201 status code means the resource was created successfully
        self.wfile.write(json.dumps({"message": "Item added successfully!"}).encode('utf-8'))
"""        
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
        
        """# Handling the PUT request to edit groceries
    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])  # Gets the size of the incoming data
        put_data = self.rfile.read(content_length)  # Reads the incoming data based on its length
        data = json.loads(put_data)  # Decodes the JSON data into a Python dictionary

        # Extracting data from the JSON payload
        category = data['category']
        new_g_item = data['new_g_item']
        new_amount = data['new_amount']
        current_g_item = data['current_g_item']
        
        # Connecting to the SQLite database
        connect = sqlite3.connect("grocerylist.db")
        cursor = connect.cursor()  # Creating a cursor object to execute SQL commands
        
        # Updating the data in the appropriate table based on the category
        if category == 'Food':
            cursor.execute("UPDATE Food SET food = ?, amount = ? WHERE food = ?", (new_g_item, new_amount, current_g_item))
        elif category == 'Nonfood':
            cursor.execute("UPDATE Nonfood SET item = ?, amount = ? WHERE item = ?", (new_g_item, new_amount, current_g_item))
        
        # Committing the transaction and closing the connection
        connect.commit()
        connect.close()
        
        # Sending a response back to the client
        self._set_response()  # Default status is 200 (OK)
        self.wfile.write(json.dumps({"message": "Item updated successfully!"}).encode('utf-8'))

"""    
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
        """# Handling the DELETE request to remove groceries
    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])  # Gets the size of the incoming data
        delete_data = self.rfile.read(content_length)  # Reads the incoming data based on its length
        data = json.loads(delete_data)  # Decodes the JSON data into a Python dictionary

        # Extracting data from the JSON payload
        category = data['category']
        g_item = data['g_item']
        
        # Connecting to the SQLite database
        connect = sqlite3.connect("grocerylist.db")
        cursor = connect.cursor()  # Creating a cursor object to execute SQL commands
        
        # Deleting the data from the appropriate table based on the category
        if category == 'Food':
            cursor.execute("DELETE FROM Food WHERE food = ?", (g_item,))
        elif category == 'Nonfood':
            cursor.execute("DELETE FROM Nonfood WHERE item = ?", (g_item,))
        
        # Committing the transaction and closing the connection
        connect.commit()
        connect.close()
        
        # Sending a response back to the client
        self._set_response()  # Default status is 200 (OK)
        self.wfile.write(json.dumps({"message": "Item deleted successfully!"}).encode('utf-8'))"""   
           
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




"""# Function to start the HTTP server
def run(server_class=HTTPServer, handler_class=GroceryHandler, port=8080):
    server_address = ('', port)  # Setting up the server to listen on all available IP addresses and the specified port
    httpd = server_class(server_address, handler_class)  # Creating an instance of HTTPServer with the specified address and handler
    print(f'Starting server on port {port}...')  # Logging the server start
    httpd.serve_forever()  # Starting the server loop, which will keep running to handle incoming requests"""


    
    
    
if __name__ == "__main__":
    main()  # Run the server when the script is executed