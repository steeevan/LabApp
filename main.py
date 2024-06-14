import pandas as pd
import os

class CSVFileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def create_csv(self, header):    #Create a new CSV file with the specified header
        df = pd.DataFrame(columns=header)
        df.to_csv(self.file_path, index=False)
        print(f"CSV file '{self.file_path}' created with header: {header}")
    
    def read_csv(self):
        try:
            df = pd.read_csv(self.file_path)   #Read and print the contents of the CSV file
            print(df)
        except FileNotFoundError:  # Handles the case where the file does not exist
            print(f"File '{self.file_path}' does not exist.")
    
    def add_row(self, row):   #Add a new row to the CSV file
        try:
            df = pd.read_csv(self.file_path)
            new_df = pd.DataFrame([row], columns=df.columns)
            df = pd.concat([df, new_df], ignore_index=True)
            df.to_csv(self.file_path, index=False)
            print(f"Row added: {row}")
        except FileNotFoundError:           #Handles the error where the file don't exist
            print(f"File '{self.file_path}' does not exist.")

    
    def update_row(self, row_num, new_row):   #Update a specific row in the CSV file
        try:
            df = pd.read_csv(self.file_path)
            df.loc[row_num] = new_row
            df.to_csv(self.file_path, index=False)
            print(f"Row {row_num} updated to: {new_row}")
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")    # Handles the case where the file does not exist
        except IndexError:
            print(f"Row number {row_num} is out of range.")      # Handles the case where the row number is too big or too small
    
    def delete_row(self, row_num):    #Delete a specific row from the CSV file
        try:
            df = pd.read_csv(self.file_path)
            deleted_row = df.loc[row_num].to_dict()
            df = df.drop(row_num).reset_index(drop=True)
            df.to_csv(self.file_path, index=False)
            print(f"Row {row_num} deleted: {deleted_row}")     # Prints out the deleted row
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")  # Handles the case where the file does not exist
        except IndexError:
            print(f"Row number {row_num} is out of range.")    # Handles the case where the row number is out of range
    
    def delete_csv(self):    #Delete the entire CSV file
        try:
            os.remove(self.file_path)
            print(f"CSV file '{self.file_path}' deleted.")     # Prints a message indicating that the file was deleted
        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")   # Handles the case where the file does not exist.


#Example usage
# csv_manager = CSVFileManager('student.csv')   # Creates an instance of CSVFileManager with the file path 'student.csv'
# csv_manager.create_csv(['Student name','Level', 'Time', 'Session Date', 'Subject', 'Title', 'Description', 'Score', 'Instructor'])   # Creates a CSV file with the header
# csv_manager.add_row(['William', '3','Monday', '6/14', 'Small Youtuber', 'obs studio', 'Learned how to do the stuff for the small yt content creator', '10/10', 'Mr.Estavan'])   # Adds a row to the CSV file
# csv_manager.add_row(['William', '3','Tuesday', '6/15', 'Small Youtuber', 'youtube studio', 'edited video they recorded for roblox', '9/10', 'Mr.Estavan'])   # Adds another row to the CSV file
# csv_manager.read_csv()   # Reads and prints the contents of the CSV file
# csv_manager.update_row(1, ['Austin', '3','Tuesday', '6/15', 'Small Youtuber', 'obs studio', 'edited video they recorded for roblox', '9/10', 'Mr.Estavan'])   # Updates a row in the CSV file
# csv_manager.read_csv()   # Reads and prints the contents of the CSV file again
# csv_manager.delete_row(0)   # Deletes a row from the CSV file
# csv_manager.read_csv()   # Reads and prints the contents of the CSV file after deletion
# csv_manager.delete_csv()   # Deletes the entire CSV file