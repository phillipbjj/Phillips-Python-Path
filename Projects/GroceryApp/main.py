from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3


    
    #ADD LAST PRICE FOR AFTER PURCHASE OF GROCERIES, CAN BE TURNED INTO A REPRESENTATION MODEL LATER
def main():
    
    #Inherits pythons HTTP handler as a subclass for HTTP operations
    class GroceryHandler(BaseHTTPRequestHandler):
        
        def _set_response(self, status=200, content_type='application/json'):  # Default status is 200 (OK)
            self.send_response(status)  # Sends the HTTP status code
            self.send_header('Content-type', content_type)  # Specifies that the content is JSON
            self.end_headers()  # Ends the headers section, ready to send content
        
        #Handling the GET request to view the webpage and database contents
        def do_GET(self):
            #Open and read the index.html file
            with open('index.html', 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read()) #Write the content of the file to the response
                
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            category = data.get('category')
            g_item = data.get('g_item')
            amount = data.get('amount')
            
            self.add_groceries(category, g_item, amount)    #Performs the actual POST functions purpose
            self._set_response(201)
            self.wfile.write(json.dumps({"message": "Item added successfully!"}).encode('utf-8'))
            
        def do_PUT(self):
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            data = json.loads(put_data)
            
            category = data.get('category')
            new_g_item = data.get('new_g_item')
            new_amount = data.get('new_amount')
            current_g_item = data.get('current_g_item')
            
            self.edit_groceries(category, new_g_item, new_amount, current_g_item)
            self._set_response()
            self.wfile.write(json.dumps({"message": "Item updated successfully!"}).encode('utf-8'))    
            
        def do_DELETE(self):
            content_length = int(self.headers['Content-Length'])
            delete_data = self.rfile.read(content_length)
            data = json.loads(delete_data)
            
            category = data.get('category')
            g_item = data.get('g_item')
            
            self.remove_groceries(category, g_item)
            self._set_response()
            self.wfile.write(json.dumps({"message": "Item deleted successfully!"}).encode('utf-8'))    
        #Add groceries into one of the 2 categories(tables)
        def add_groceries(self, category, g_item, amount):    #POST
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
        def edit_groceries(self, category, new_g_item, new_amount, current_g_item):   #PUT
            #Need to add api interaction with website for categories
            connect = sqlite3.connect("grocerylist.db")
            cursor = connect.cursor()
            if category == 'Food':
                cursor.execute("UPDATE Food SET food = ?, amount = ?,  WHERE food = ?", (new_g_item, new_amount, current_g_item))
            elif category == 'Nonfood':
                cursor.execute("UPDATE Nonfood SET item = ?, amount = ?, WHERE item = ?", (new_g_item, new_amount, current_g_item))
            
            connect.commit()
            connect.close()  
        
        #Remove groceries from the list
        def remove_groceries(self, category, g_item):
            connect = sqlite3.connect("grocerylist.db")
            cursor = connect.cursor()
            if category == 'Food':
                cursor.execute("DELETE FROM Food WHERE food = ?", (g_item,))
            elif category == 'Nonfood':
                cursor.execute("DELETE FROM Nonfood WHERE item = ?", (g_item,))
            
            connect.commit()
            connect.close()  

    # Function to start the HTTP server
    def run(server_class=HTTPServer, handler_class=GroceryHandler, port=8000):
        server_address = ('', port)  # Setting up the server to listen on all available IP addresses and the specified port
        httpd = server_class(server_address, handler_class)  # Creating an instance of HTTPServer with the specified address and handler
        print(f'Starting server on port {port}...')  # Logging the server start
        httpd.serve_forever()  # Starting the server loop, which will keep running to handle incoming requests

    run()
    
if __name__ == "__main__":
    main()