from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handles GET requests
    def do_GET(self):
        if self.path == '/grocerylist':
            self.get_grocery_list()  # Call function to retrieve the grocery list from SQLite3
        else:
            self.serve_file()  # Serve static files (HTML, CSS, JS) to the client

    def serve_file(self):
        # Serve the main HTML file or other static files
        if self.path == '/':
            self.path = '/index.html'  # Default to index.html for the root path
        try:
            with open(self.path[1:], 'rb') as file:  # Open the requested file, stripping the leading '/'
                self.send_response(200)  # Send an OK response status
                if self.path.endswith('.html'):
                    self.send_header('Content-type', 'text/html')  # Set content type for HTML
                elif self.path.endswith('.css'):
                    self.send_header('Content-type', 'text/css')  # Set content type for CSS
                elif self.path.endswith('.js'):
                    self.send_header('Content-type', 'application/javascript')  # Set content type for JavaScript
                else:
                    self.send_header('Content-type', 'text/plain')  # Default content type
                self.end_headers()
                self.wfile.write(file.read())  # Write the file content to the response
        except Exception as e:
            self.send_response(404)  # File not found, send a 404 response
            self.end_headers()

    def get_grocery_list(self):
        # Connect to SQLite3 database and retrieve the grocery list
        conn = sqlite3.connect('grocerylist.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grocerylist")  # Query all rows from the grocerylist table
        rows = cursor.fetchall()  # Fetch all rows from the query result
        conn.close()  # Close the database connection
        
        # Respond with the grocery list in JSON format
        self.send_response(200)  # Send an OK response status
        self.send_header('Content-type', 'application/json')  # Set content type to JSON
        self.end_headers()
        self.wfile.write(json.dumps(rows).encode())  # Convert rows to JSON and send as response

    # Handles POST requests to add new grocery items
    def do_POST(self):
        if self.path == '/add':
            content_length = int(self.headers['Content-Length'])  # Get the length of the request body
            post_data = self.rfile.read(content_length)  # Read the request body
            data = json.loads(post_data.decode('utf-8'))  # Decode and parse the JSON data
            item = data.get('item')  # Extract the item name from the parsed data
            quantity = data.get('quantity')  # Extract the quantity from the parsed data

            # Connect to SQLite3 database and insert the new item
            conn = sqlite3.connect('grocerylist.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO grocerylist (item, quantity) VALUES (?, ?)", (item, quantity))
            conn.commit()  # Commit the changes to the database
            conn.close()  # Close the database connection
            
            self.send_response(200)  # Send an OK response status
            self.end_headers()

# Function to run the HTTP server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)  # Define the server address and port
    httpd = server_class(server_address, handler_class)  # Create the HTTP server
    print(f'Starting server on port {port}...')  # Print a message indicating the server is starting
    httpd.serve_forever()  # Start the server, keeping it running indefinitely

if __name__ == '__main__':
    run()  # Run the server when the script is executed
