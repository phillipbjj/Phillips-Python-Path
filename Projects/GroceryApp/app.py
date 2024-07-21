from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import urllib.parse
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as file:
                self.wfile.write(file.read().encode())
        elif self.path == '/styles.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('styles.css', 'r') as file:
                self.wfile.write(file.read().encode())
        elif self.path == '/items':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            conn = sqlite3.connect('grocery.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM items')
            items = cursor.fetchall()
            conn.close()
            self.wfile.write(json.dumps(items).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(post_data.decode())
        if self.path == '/add':
            item = data['item'][0]
            category = data['category'][0]
            quantity = data['quantity'][0]
            conn = sqlite3.connect('grocery.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO items (item, category, quantity) VALUES (?, ?, ?)', (item, category, quantity))
            conn.commit()
            conn.close()
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        elif self.path == '/delete':
            item_id = data['id'][0]
            conn = sqlite3.connect('grocery.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
            conn.commit()
            conn.close()
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    conn = sqlite3.connect('grocery.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, item TEXT, category TEXT, quantity INTEGER)')
    conn.commit()
    conn.close()
    run()
