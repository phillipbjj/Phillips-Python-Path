from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import json

class GroceryListHandler(BaseHTTPRequestHandler):
    # Set HTTP headers
    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    # Handle GET requests
    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            items = self.get_items()
            self.wfile.write(self.render_template(items).encode('utf-8'))
        elif self.path == '/static/style.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('static/style.css', 'r') as file:
                self.wfile.write(file.read().encode('utf-8'))

    # Handle POST requests
    def do_POST(self):
        if self.path == '/add_item':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            self.add_item(data['name'], data['quantity'])
            self._set_headers('application/json')
            items = self.get_items()
            self.wfile.write(json.dumps({'items': items}).encode('utf-8'))

    # Handle DELETE requests
    def do_DELETE(self):
        if self.path.startswith('/delete_item/'):
            item_id = int(self.path.split('/')[-1])
            self.delete_item(item_id)
            self._set_headers('application/json')
            items = self.get_items()
            self.wfile.write(json.dumps({'items': items}).encode('utf-8'))

    # Render the HTML template
    def render_template(self, items):
        with open('templates/index.html', 'r') as file:
            template = file.read()
        item_list_html = ''.join(
            f'<li><span>{item[1]} <span class="quantity">x{item[2]}</span></span> <button onclick="deleteItem({item[0]})" class="delete-btn">🗑️</button></li>'
            for item in items
        )
        return template.replace('{{ items }}', item_list_html)

    # Retrieve items from the database
    def get_items(self):
        conn = sqlite3.connect('grocery_list.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        items = cursor.fetchall()
        conn.close()
        return items

    # Add an item to the database
    def add_item(self, name, quantity):
        conn = sqlite3.connect('grocery_list.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        conn.close()

    # Delete an item from the database
    def delete_item(self, item_id):
        conn = sqlite3.connect('grocery_list.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
        conn.commit()
        conn.close()

# Initialize the database
def init_db():
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       quantity INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

# Run the server
def run(server_class=HTTPServer, handler_class=GroceryListHandler, port=8000):
    server_address = ('', port)  # '' means bind to all available interfaces
    httpd = server_class(server_address, handler_class)
    print(f'Starting http on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    init_db()
    run()
