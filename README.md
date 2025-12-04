# Student Record Management System (SRMS)

A secure, role-based Python application for managing student records with authentication and authorization.

## Features

### Authentication & Authorization
- **Secure Login System** - Bcrypt password hashing
- **Role-Based Access Control** - Admin, Staff, and Guest roles
- **Admin Signup** - Create administrator accounts
- **Staff Signup** - Register staff members
- **Guest Access** - View-only mode without registration

### Record Management
- **Add New Records** - Create student records with ID, name, course, and grade
- **View All Records** - Display records in formatted table
- **Search Records** - Find specific records by student ID
- **Update Records** - Modify existing student information
- **Delete Records** - Remove individual records
- **Delete All Records** - Bulk deletion (admin-only)

### User Management (Admin Only)
- **View All Users** - Display all registered users
- **Delete Users** - Remove user accounts (with safety checks)

## How to Run

1. Install dependencies:
   ```bash
   pip install bcrypt
   ```

2. Run the program:
   ```bash
   python main.py
   ```

3. First-time setup:
   - Select option 1 to create an admin account
   - Login with your admin credentials
   - Start managing records or create staff accounts

## Default Login Credentials

For testing purposes, you can use these default credentials:
- **Username**: admin
- **Password**: 1234

## User Roles & Permissions

| Feature | Admin | Staff | Guest |
|---------|-------|-------|-------|
| Create Record | ✓ | ✓ | ✗ |
| View All Records | ✓ | ✓ | ✓ |
| Search Record | ✓ | ✓ | ✗ |
| Update Record | ✓ | ✓ | ✗ |
| Delete Record | ✓ | ✓ | ✗ |
| Delete All Records | ✓ | ✗ | ✗ |
| View All Users | ✓ | ✗ | ✗ |
| Delete Users | ✓ | ✗ | ✗ |

## Menu Options

### Authentication Menu
1. **Admin Signup** - Create administrator account
2. **Staff Signup** - Create staff account
3. **Login** - Login with credentials
4. **Guest Login** - View-only access
5. **Exit** - Close the application

### Main Menu (Admin/Staff)
1. **Create Record** - Add new student record
2. **View All Records** - Display all records
3. **Search Record** - Find record by ID
4. **Update Record** - Modify existing record
5. **Delete Record** - Remove single record
6. **Delete All Records** - Remove all records (Admin only)
7. **View All Users** - Display all users (Admin only)
8. **Delete User** - Remove user account (Admin only)
0. **Logout** - Return to authentication menu

### Guest Menu
1. **View All Records** - Browse student records
0. **Logout** - Return to authentication menu

## Data Storage

- `users.json` - Stores user credentials and roles
- `records.json` - Stores student records

Both files are created automatically when needed.

## Security Features

- **Password Hashing** - Bcrypt encryption for secure storage
- **Password Confirmation** - Double-entry verification during signup
- **Access Control** - Role-based permissions on all operations
- **Safe Deletion** - Confirmation prompts for destructive actions
- **Admin Protection** - Cannot delete own account or last admin
- **Input Validation** - Prevents empty fields and duplicates

## Example Usage

### Creating a Record
```
Enter Student ID: 101
Enter Name: John Doe
Enter Course: Computer Science
Enter Grade: A
```

### Viewing Records
```
ID         Name                 Course          Grade      Created             
---------------------------------------------------------------------------
1        Hit                      cse             A          2025-12-04 10:30:00
2        Kt                       cse             B          2025-12-04 10:35:00
```

## Requirements

- Python 3.7 or higher
- bcrypt library 

## Project Structure

```
SRMS/
├── main.py              # Main application file
├── users.json           # User database (auto-generated)
├── records.json         # Student records (auto-generated)
└── README.md            # This file
```

## License

This project is open source and available for educational purposes.
