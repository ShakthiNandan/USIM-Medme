from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

DATABASE = 'discharged_patients.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def discharged_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    return render_template('discharged_patients.html', patients=patients)

@app.route('/view_report/<int:id>')
def view_report(id):
    conn = get_db_connection()
    patient = conn.execute('SELECT * FROM patients WHERE id = ?', (id,)).fetchone()
    conn.close()
    if patient is None:
        flash('Patient not found!')
        return redirect(url_for('discharged_patients'))
    return render_template('report.html', patient=patient)

@app.route('/re_admit/<int:id>', methods=['POST'])
def re_admit(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM patients WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Patient re-admitted successfully.')
    return redirect(url_for('discharged_patients'))

if __name__ == '__main__':
    app.run(debug=True)
