from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS intravenous_access (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT)''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to save the selected intravenous access type
@app.route('/save', methods=['POST'])
def save_access():
    access_type = request.form['access_type']
    
    # Insert data into the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO intravenous_access (type) VALUES (?)', (access_type,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Data saved successfully"})

# Route to retrieve stored data
@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM intravenous_access')
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
