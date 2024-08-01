# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class GroceryRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/grocery-list':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open('grocery_list.json', 'r') as f:
                self.wfile.write(f.read().encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/update-list':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            with open('grocery_list.json', 'wb') as f:
                f.write(post_data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Success')

def run(server_class=HTTPServer, handler_class=GroceryRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting server on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
