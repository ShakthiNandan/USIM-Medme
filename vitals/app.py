from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('vital_signs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vitals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            value1 REAL,
            value2 REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_vital', methods=['POST'])
def save_vital():
    data = request.json
    type_ = data.get('type')
    value1 = data.get('value1')
    value2 = data.get('value2')
    
    conn = sqlite3.connect('vital_signs.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO vitals (type, value1, value2) VALUES (?, ?, ?)', (type_, value1, value2))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
