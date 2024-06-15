import pandas as pd
import os
import csv

class CSVFileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def create_csv(self, header):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
            print(f"CSV file '{self.file_path}' created with header: {header}")
    
    def read_csv(self):
        try:
            df = pd.read_csv(self.file_path)
            print(df)
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")
    
    def add_row(self, row):
        try:
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row)
            print(f"Row added: {row}")
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")
    
    def update_row(self, row_num, new_row):
        try:
            df = pd.read_csv(self.file_path)
            df.loc[row_num] = new_row
            df.to_csv(self.file_path, index=False)
            print(f"Row {row_num} updated to: {new_row}")
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")
        except IndexError:
            print(f"Row number {row_num} is out of range.")
    
    def delete_row(self, row_num):
        try:
            df = pd.read_csv(self.file_path)
            deleted_row = df.loc[row_num].to_dict()
            df = df.drop(row_num).reset_index(drop=True)
            df.to_csv(self.file_path, index=False)
            print(f"Row {row_num} deleted: {deleted_row}")
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")
        except IndexError:
            print(f"Row number {row_num} is out of range.")
    
    def delete_csv(self):
        try:
            os.remove(self.file_path)
            print(f"CSV file '{self.file_path}' deleted.")
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")

# Example usage
# csv_manager = CSVFileManager('student_evaluations.csv')
# csv_manager.create_csv(['Name', 'Level', 'Subject', 'Rating', 'Title', 'Description', 'Instructor', 'Comments'])
# csv_manager.add_row(['William', '3', 'English', '5', 'Youtuber', 'created video with roblox recording and edited it with canva and capcut', 'Estevan', 'Great job'])
# csv_manager.read_csv()
# csv_manager.update_row(1, ['Austin', '3', 'Tuesday', '6/15', 'Small Youtuber', 'obs studio', 'edited video they recorded for roblox', '9/10', 'Mr. Estevan'])
# csv_manager.read_csv()
# csv_manager.delete_row(0)
# csv_manager.read_csv()
# csv_manager.delete_csv()
