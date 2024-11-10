import sqlite3

DATABASE = './database/users.db'

# Function to connect to SQLite
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Function to initialize the users table
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        ''')
    print("Database initialized.")

# Function to add a new user
def add_user(email, password):
    try:
        with get_db_connection() as conn:
            conn.execute(
                'INSERT INTO users (email, password) VALUES (?, ?)',
                (email, password)
            )
        print(f"User '{email}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: User with email '{email}' already exists.")

# Function to view all users
def view_users():
    with get_db_connection() as conn:
        users = conn.execute('SELECT * FROM users').fetchall()
        if users:
            print(f"{'ID':<5} {'Email':<30} {'Password':<20}")
            print("-" * 55)
            for user in users:
                print(f"{user['id']:<5} {user['email']:<30} {user['password']:<20}")
        else:
            print("No users found in the database.")

# Function to delete a user by email
def delete_user(email):
    with get_db_connection() as conn:
        result = conn.execute('DELETE FROM users WHERE email = ?', (email,))
        if result.rowcount > 0:
            print(f"User '{email}' deleted successfully.")
        else:
            print(f"User '{email}' not found.")

# Main function with options
def main():
    while True:
        print("\nDatabase Management Menu")
        print("1. Initialize Database")
        print("2. Add User")
        print("3. View Users")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            init_db()
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            add_user(email, password)
        elif choice == '3':
            view_users()
        elif choice == '4':
            email = input("Enter email to delete: ")
            delete_user(email)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
