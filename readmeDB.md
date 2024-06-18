import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        birthdate TEXT NOT NULL,
        first_day TEXT NOT NULL,
        level TEXT NOT NULL
    )
''')

# Create Parents table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS parents (
        parent_id INTEGER PRIMARY KEY,
        student_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (student_id)
    )
''')

# Create Instructors table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS instructors (
        instructor_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
