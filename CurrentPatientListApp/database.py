
import sqlite3

def init_db():
    # Connect to SQLite database
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    # Create patients table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ic_passport TEXT NOT NULL,
        admitted_date TEXT NOT NULL,
        remarks TEXT
    )
    ''')
    conn.commit()
    conn.close()

def add_patient(name, ic_passport, admitted_date, remarks):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, ic_passport, admitted_date, remarks) VALUES (?, ?, ?, ?)", 
                   (name, ic_passport, admitted_date, remarks))
    conn.commit()
    conn.close()

def get_patients():
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.close()
    return patients

def edit_patient(patient_id, name, ic_passport, remarks):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE patients SET name = ?, ic_passport = ?, remarks = ? WHERE id = ?", 
                   (name, ic_passport, remarks, patient_id))
    conn.commit()
    conn.close()

def discharge_patient(patient_id):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
    conn.commit()
    conn.close()
