import unittest
import os
from database_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    """
    Test suite for the DatabaseManager class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.db_file = 'test_database.db'
        self.db_manager = DatabaseManager(self.db_file)
        self.db_manager.create_connection()

        # Create a test table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value INTEGER
        );
        """
        self.db_manager.execute_query(create_table_query)

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.db_manager.close_connection()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_insert_and_query(self):
        """
        Test inserting data into the database and querying it.
        """
        insert_query = "INSERT INTO test_table (name, value) VALUES (?, ?)"
        data = ("test_name", 123)
        self.assertTrue(self.db_manager.execute_query(insert_query, data))

        select_query = "SELECT * FROM test_table WHERE name = ?"
        result = self.db_manager.execute_read_query(select_query, ("test_name",))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "test_name")
        self.assertEqual(result[0][2], 123)

    def test_update(self):
        """
        Test updating data in the database.
        """
        insert_query = "INSERT INTO test_table (name, value) VALUES (?, ?)"
        data = ("test_name", 123)
        self.db_manager.execute_query(insert_query, data)

        update_query = "UPDATE test_table SET value = ? WHERE name = ?"
        self.assertTrue(self.db_manager.execute_query(update_query, (456, "test_name")))

        select_query = "SELECT * FROM test_table WHERE name = ?"
        result = self.db_manager.execute_read_query(select_query, ("test_name",))
        self.assertEqual(result[0][2], 456)

    def test_delete(self):
        """
        Test deleting data from the database.
        """
        insert_query = "INSERT INTO test_table (name, value) VALUES (?, ?)"
        data = ("test_name", 123)
        self.db_manager.execute_query(insert_query, data)

        delete_query = "DELETE FROM test_table WHERE name = ?"
        self.assertTrue(self.db_manager.execute_query(delete_query, ("test_name",)))

        select_query = "SELECT * FROM test_table WHERE name = ?"
        result = self.db_manager.execute_read_query(select_query, ("test_name",))
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
