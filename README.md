# Student Record Management System (SRMS)

A simple Python-based record management system for managing student records.

## Features

-  Add new student records
-  View all records
-  Search records by student ID
-  Update existing records
-  Delete records
-  Data persistence using JSON

## How to Run

1. Open terminal in the project directory
2. Run the program:
   ```
   python main.py
   ```

## Usage

The system provides a menu-driven interface with 6 options:

1. **Add New Record** - Enter student ID, name, course, and grade
2. **View All Records** - Display all stored records in a table
3. **Search Record** - Find a specific record by student ID
4. **Update Record** - Modify existing record details
5. **Delete Record** - Remove a record from the system
6. **Exit** - Close the program

## Data Storage

Records are stored in `records.json` file in the same directory. The file is created automatically when you add the first record.

## Example

```
Student ID: S001
Name: John Doe
Course: Computer Science
Grade: A
```

## Requirements

- Python 3.x (no external dependencies required)
