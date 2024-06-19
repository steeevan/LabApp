import sqlite3
from sqlite3 import Error

class DatabaseManager:
    """
    A class to manage and connect to a SQLite database.
    """

    def __init__(self, db_file):
        """
        Initializes the DatabaseManager with the specified database file.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.db_file = db_file
        self.conn = None

    def create_connection(self):
        """
        Creates a connection to the SQLite database.

        Returns:
            Connection object or None.
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"Connection to SQLite DB '{self.db_file}' successful")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to SQLite DB")
            self.conn = None
        return self.conn

    def close_connection(self):
        """
        Closes the connection to the SQLite database.
        """
        if self.conn:
            self.conn.close()
            print("Connection to SQLite DB closed")

    def execute_query(self, query, params=None):
        """
        Executes a SQL query.

        Args:
            query (str): The SQL query to execute.
            params (tuple): Optional parameters to bind to the query.

        Returns:
            True if the query was executed successfully, False otherwise.
        """
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
        """
        Executes a SQL read query and returns the result.

        Args:
            query (str): The SQL query to execute.
            params (tuple): Optional parameters to bind to the query.

        Returns:
            list of tuples containing the query result.
        """
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

# Example usage
# Uncomment the following lines to see the class in action
'''
db_manager = DatabaseManager('example.db')
db_manager.create_connection()
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""
db_manager.execute_query(create_table_query)
insert_user_query = "INSERT INTO users (name, age, gender, nationality) VALUES (?, ?, ?, ?)"
user_data = ("James", 25, "male", "USA")
db_manager.execute_query(insert_user_query, user_data)
select_users_query = "SELECT * FROM users"
users = db_manager.execute_read_query(select_users_query)
print(users)
db_manager.close_connection()
'''