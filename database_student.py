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

students = [
    (1, 'John Doe', '2005-01-15', '2024-06-01', 'Rookie'),
    (2, 'Jane Smith', '2004-02-20', '2024-06-01', 'Advanced'),
    (3, 'Michael Brown', '2003-03-25', '2024-06-01', 'Intermediate'),
    (4, 'Emily Davis', '2002-04-30', '2024-06-01', 'Rookie'),
    (5, 'Chris Wilson', '2005-05-05', '2024-06-01', 'Rookie'),
    (6, 'Anna Moore', '2004-06-10', '2024-06-01', 'Intermediate'),
    (7, 'James Taylor', '2003-07-15', '2024-06-01', 'Advanced'),
    (8, 'Laura Anderson', '2002-08-20', '2024-06-01', 'Advanced'),
    (9, 'David Lee', '2005-09-25', '2024-06-01', 'Intermediate'),
    (10, 'Emma Martin', '2004-10-30', '2024-06-01', 'Rookie')
]

# Insert students into the table
cursor.executemany('''
    INSERT INTO students (student_id, name, birthdate, first_day, level) VALUES (?, ?, ?, ?, ?)
''', students)

# Commit changes and close connection
conn.commit()
conn.close()
