import sqlite3


# Connect to SQLite database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create Instructors table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS instructors (
        instructor_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
''')

# Define instructor data
instructors = [
    (1, 'Alice Johnson', 'alice.johnson@example.com', '555-1111'),
    (2, 'Bob Williams', 'bob.williams@example.com', '555-2222'),
    (3, 'Charlie Brown', 'charlie.brown@example.com', '555-3333'),
    (4, 'Diana Prince', 'diana.prince@example.com', '555-4444')
]

# Insert instructors into the table
cursor.executemany('''
    INSERT INTO instructors (instructor_id, name, email, phone_number) VALUES (?, ?, ?, ?)
''', instructors)

# Commit changes and close connection
conn.commit()
conn.close()