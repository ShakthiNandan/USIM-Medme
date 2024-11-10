from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = './database/users.db'

# Function to connect to SQLite
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with get_db_connection() as conn:
            user = conn.execute(
                'SELECT * FROM users WHERE email = ? AND password = ?', (email, password)
            ).fetchone()

        if user:
            session['user_id'] = user['id']
            session['user_email'] = user['email']
            flash('Login successful!', 'success')
            return redirect('/dashboard')
        else:
            flash('Invalid email or password.', 'error')
            return redirect('/')

    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user_email = session.get('user_email', 'Unknown User')
    patient_name = "John Doe"
    doctor_names = ["Dr. Smith", "Dr. Adams", "Dr. Johnson"]

    return render_template(
        'dashboard.html',
        user_email=user_email,
        patient_name=patient_name,
        doctor_names=doctor_names
    )

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
