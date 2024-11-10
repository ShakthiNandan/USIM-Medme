import sqlite3

# Connect to the database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('discharged_patients.db')

# Create the patients table
conn.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ic_no TEXT NOT NULL,
    last_discharged TEXT NOT NULL
)
""")

# Insert some sample data
conn.execute("INSERT INTO patients (name, ic_no, last_discharged) VALUES ('John Doe', 'A1234567', '2024-11-01')")
conn.execute("INSERT INTO patients (name, ic_no, last_discharged) VALUES ('Jane Smith', 'B2345678', '2024-10-15')")
conn.commit()
conn.close()

print("Database initialized and sample data added.")
