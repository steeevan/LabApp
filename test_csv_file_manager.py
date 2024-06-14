import unittest
import os
import pandas as pd
import random
import string
from main import CSVFileManager  # Ensure the CSVFileManager class is in a file named csv_file_manager.py

class TestCSVFileManager(unittest.TestCase):

    def setUp(self):
        """Set up a test environment for each test."""
        self.columns = ['Student name', 'Level', 'Time', 'Session Date', 'Subject', 'Title', 'Description', 'Score', 'Instructor']
        self.test_files = []
        self.new_directory = 'test_directory'
        
        if not os.path.exists(self.new_directory):
            os.makedirs(self.new_directory)

    def tearDown(self):
        """Clean up the test environment after each test."""
        for file in self.test_files:
            if os.path.exists(file):
                os.remove(file)
        
        if os.path.exists(self.new_directory):
            for file in os.listdir(self.new_directory):
                os.remove(os.path.join(self.new_directory, file))
            os.rmdir(self.new_directory)

    def random_string(self, length=8):
        """Generate a random string of fixed length."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def create_random_csv_file(self, num_rows):
        """Create a CSV file with a random number of entries."""
        file_name = f'{self.random_string()}.csv'
        self.test_files.append(file_name)
        csv_manager = CSVFileManager(file_name)
        csv_manager.create_csv(self.columns)
        
        for _ in range(num_rows):
            row = [
                self.random_string(),  # Student name
                str(random.randint(1, 5)),  # Level
                random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),  # Time
                f'6/{random.randint(1, 30)}',  # Session Date
                'Small Youtuber',  # Subject
                random.choice(['obs studio', 'youtube studio', 'editing']),  # Title
                'Learned how to do the stuff for the small yt content creator',  # Description
                f'{random.randint(1, 10)}/10',  # Score
                'Mr.Estavan'  # Instructor
            ]
            csv_manager.add_row(row)
        
        return file_name

    def test_create_random_csv_files(self):
        """Test creating multiple CSV files with random entries."""
        num_files = 5
        for _ in range(num_files):
            num_rows = random.randint(1, 10)
            file_name = self.create_random_csv_file(num_rows)
            df = pd.read_csv(file_name)
            self.assertEqual(len(df), num_rows)

    def test_save_csv_to_directory(self):
        """Test saving the CSV file to a new directory."""
        num_rows = random.randint(1, 10)
        file_name = self.create_random_csv_file(num_rows)
        csv_manager = CSVFileManager(file_name)
        csv_manager.save_csv_to_directory(self.new_directory)
        new_file_path = os.path.join(self.new_directory, file_name)
        self.assertTrue(os.path.exists(new_file_path))
        df = pd.read_csv(new_file_path)
        self.assertEqual(len(df), num_rows)

if __name__ == '__main__':
    unittest.main()
