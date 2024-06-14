# CSVFileManager Documentation

## CSVFileManager Class

### Overview

A class to manage CSV file operations including creating, reading, adding, updating, and deleting rows, as well as deleting the entire CSV file.

### Attributes

- `file_path`: The path to the CSV file.

### Methods

#### `__init__(self, file_path)`
Initializes the CSVFileManager with the specified file path.

- **Input:**
  - `file_path` (str): The path to the CSV file.

#### `create_csv(self, header)`
Creates a new CSV file with the specified header.

- **Input:**
  - `header` (list of str): A list of column names for the CSV file.

#### `read_csv(self)`
Reads and prints the contents of the CSV file.

#### `add_row(self, row)`
Adds a new row to the CSV file.

- **Input:**
  - `row` (list): A list representing the new row to be added.

#### `update_row(self, row_num, new_row)`
Updates a specific row in the CSV file.

- **Input:**
  - `row_num` (int): The index of the row to update.
  - `new_row` (list): A list representing the new row data.

#### `delete_row(self, row_num)`
Deletes a specific row from the CSV file.

- **Input:**
  - `row_num` (int): The index of the row to delete.

#### `delete_csv(self)`
Deletes the entire CSV file.

---

## TestCSVFileManager Class

### Overview

Test suite for the CSVFileManager class.

### Test Cases

#### `test_initialization(self)`
Verifies that the CSVFileManager initializes with the correct file path.

#### `test_create_csv(self)`
Verifies that a CSV file is created with the specified header.

#### `test_read_csv(self)`
Verifies that reading a CSV file returns the correct contents.

#### `test_add_row(self)`
Verifies that adding a row to the CSV file works correctly.

#### `test_update_row(self)`
Verifies that updating a specific row in the CSV file works correctly.

#### `test_delete_row(self)`
Verifies that deleting a specific row from the CSV file works correctly.

#### `test_delete_csv(self)`
Verifies that the entire CSV file can be deleted.
