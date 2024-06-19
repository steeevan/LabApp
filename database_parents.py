import sqlite3
from database_student import students

# Connect to SQLite database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Ensure the students table exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        birthdate TEXT NOT NULL,
        first_day TEXT NOT NULL,
        level TEXT NOT NULL
    )
''')

# Insert students if not already present
cursor.executemany('''
    INSERT OR IGNORE INTO students (student_id, name, birthdate, first_day, level) VALUES (?, ?, ?, ?, ?)
''', students)

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

# Define parent data
parents = [
    (1, 1, 'Mary Doe', 'mary.doe@example.com', '555-1234'),
    (2, 2, 'Robert Smith', 'robert.smith@example.com', '555-5678'),
    (3, 3, 'Linda Brown', 'linda.brown@example.com', '555-8765'),
    (4, 4, 'Patricia Davis', 'patricia.davis@example.com', '555-4321'),
    (5, 5, 'Michael Wilson', 'michael.wilson@example.com', '555-8765'),
    (6, 6, 'Elizabeth Moore', 'elizabeth.moore@example.com', '555-4321'),
    (7, 7, 'Charles Taylor', 'charles.taylor@example.com', '555-3456'),
    (8, 8, 'Barbara Anderson', 'barbara.anderson@example.com', '555-7890'),
    (9, 9, 'Thomas Lee', 'thomas.lee@example.com', '555-2345'),
    (10, 10, 'Jessica Martin', 'jessica.martin@example.com', '555-6789')
]

# Insert parents into the table
cursor.executemany('''
    INSERT INTO parents (parent_id, student_id, name, email, phone_number) VALUES (?, ?, ?, ?, ?)
''', parents)

# Commit changes and close connection
conn.commit()
conn.close()
