# database/database_manager.py

import sqlite3
from sqlite3 import Error
import os

class DatabaseManager:
    """
    A class to manage and connect to a SQLite database.
    """

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"Connection to SQLite DB '{self.db_file}' successful")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to SQLite DB")
            self.conn = None
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection to SQLite DB closed")

    def execute_query(self, query, params=None):
        if not self.conn:
            print("No database connection")
            return False

        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully")
            return True
        except Error as e:
            print(f"Error '{e}' occurred while executing query")
            return False

    def execute_read_query(self, query, params=None):
        if not self.conn:
            print("No database connection")
            return []

        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error '{e}' occurred while executing read query")
            return []

    # New methods for user management
    def create_user_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );
        """
        self.execute_query(create_table_query)

    def add_user(self, username, password, role):
        insert_user_query = "INSERT INTO users (username, password, role) VALUES (?, ?, ?)"
        return self.execute_query(insert_user_query, (username, password, role))

    def get_user(self, username):
        select_user_query = "SELECT * FROM users WHERE username = ?"
        users = self.execute_read_query(select_user_query, (username,))
        return users[0] if users else None


# Create the users table if it does not exist
if __name__ == "__main__":
    # Set the path for the new database in the assets folder
    os.makedirs("assets", exist_ok=True)
    db_manager = DatabaseManager("assets/users.db")
    db_manager.create_connection()
    db_manager.create_user_table()
    db_manager.close_connection()
