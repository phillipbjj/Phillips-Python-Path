from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize database
def init_db():
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       quantity INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data['name']
    quantity = data['quantity']

    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    
    # Emit the updated list to all connected clients
    socketio.emit('update_list', {'items': items})
    
    return jsonify({'message': 'Item added successfully'})

@app.route('/delete_item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()

    # Emit the updated list to all connected clients
    socketio.emit('update_list', {'items': items})

    return jsonify({'message': 'Item deleted successfully'})

@socketio.on('connect')
def handle_connect():
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    emit('update_list', {'items': items})

if __name__ == '__main__':
    init_db()
    socketio.run(app, host='0.0.0.0', port=5000)
