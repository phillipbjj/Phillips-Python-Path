from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

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

# Route for the home page
@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    # Fetch all items from the items table
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    # Render the index.html template with the fetched items
    return render_template('index.html', items=items)

# Route to handle adding an item
@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data['name']
    quantity = data['quantity']

    # Connect to the database and insert the new item
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    # Fetch the updated list of items
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()

    return jsonify({'items': items})

# Route to handle deleting an item
@app.route('/delete_item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Connect to the database and delete the specified item
    conn = sqlite3.connect('grocery_list.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    # Fetch the updated list of items
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()

    return jsonify({'items': items})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
