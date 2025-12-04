# Student Record Management System (SRMS)
## Project Report

---

## 1. Project Overview

### 1.1 Title
**Student Record Management System (SRMS)**

### 1.2 Objective
To develop a secure, role-based student record management system that allows administrators and staff to efficiently manage student academic records while providing read-only access to guests.

### 1.3 Scope
The system provides complete CRUD (Create, Read, Update, Delete) operations for student records with a secure authentication mechanism using password hashing and role-based access control.

---

## 2. System Features

### 2.1 User Management
- **Admin Signup**: Create administrator accounts with full system privileges
- **Staff Signup**: Register staff members with record management capabilities
- **User Login**: Secure authentication with password verification
- **Guest Login**: Anonymous access for viewing records only
- **Password Security**: Bcrypt hashing for secure password storage

### 2.2 Record Management
- **Create Record**: Add new student records with ID, name, course, and grade
- **View All Records**: Display all student records in formatted table
- **Search Record**: Find specific student records by ID
- **Update Record**: Modify existing student information
- **Delete Record**: Remove individual student records
- **Delete All Records**: Bulk deletion (admin-only feature)

### 2.3 Role-Based Access Control

| Feature | Admin | Staff | Guest |
|---------|-------|-------|-------|
| Create Record | ✓ | ✓ | ✗ |
| View All Records | ✓ | ✓ | ✓ |
| Search Record | ✓ | ✓ | ✗ |
| Update Record | ✓ | ✓ | ✗ |
| Delete Record | ✓ | ✓ | ✗ |
| Delete All Records | ✓ | ✗ | ✗ |

---

## 3. Technical Specifications

### 3.1 Programming Language
- **Python 3.x**

### 3.2 Dependencies
- `bcrypt`: Password hashing and verification
- `json`: Data persistence
- `os`: File system operations
- `datetime`: Timestamp generation
- `typing`: Type hints for better code quality

### 3.3 Data Storage
- **users.json**: Stores user credentials and roles
- **records.json**: Stores student academic records

### 3.4 Data Models

#### User Model
```json
{
    "username": "string",
    "password": "hashed_string",
    "role": "admin|staff|guest"
}
```

#### Record Model
```json
{
    "id": "string",
    "name": "string",
    "course": "string",
    "grade": "string",
    "created_at": "YYYY-MM-DD HH:MM:SS",
    "created_by": "username"
}
```

---

## 4. System Architecture

### 4.1 Module Structure

```
SRMS/
├── auth.py              # Main application file
├── users.json           # User database
├── records.json         # Student records database
├── README.md            # Project documentation
├── helper.md            # Helper notes
└── PROJECT_REPORT.md    # This report
```

### 4.2 Function Hierarchy

#### Authentication Module
1. `read_json_file()` - Load data from JSON files
2. `save_json_file()` - Save data to JSON files
3. `find_user()` - Locate user by username
4. `hash_pass()` - Hash passwords using bcrypt
5. `verify_pass()` - Verify password against hash
6. `enter_password()` - Password input with confirmation
7. `admin_signup()` - Register admin users
8. `staff_signup()` - Register staff users
9. `guest_login()` - Anonymous guest access
10. `login()` - Authenticate registered users

#### Record Management Module
1. `read_records()` - Load student records
2. `save_records()` - Persist student records
3. `find_record()` - Search for specific record
4. `create_record()` - Add new student record
5. `view_all_records()` - Display all records
6. `search_record()` - Find and display specific record
7. `update_record()` - Modify existing record
8. `delete_record()` - Remove single record
9. `delete_all_records()` - Bulk delete (admin-only)

#### User Interface Module
1. `display_auth_menu()` - Show authentication options
2. `display_main_menu()` - Show role-specific menu
3. `main()` - Application entry point and control flow

---

## 5. Security Features

### 5.1 Password Security
- **Bcrypt Hashing**: Industry-standard password hashing algorithm
- **Salt Generation**: Automatic salt generation for each password
- **Password Confirmation**: Double-entry verification during signup
- **No Plain Text Storage**: Passwords never stored in readable format

### 5.2 Access Control
- **Role Verification**: Every sensitive operation checks user role
- **Permission Enforcement**: Functions reject unauthorized access attempts
- **Admin Restrictions**: Critical operations limited to admin users
- **Guest Limitations**: Read-only access for anonymous users

### 5.3 Data Validation
- **Input Sanitization**: Strip whitespace from all inputs
- **Empty Field Checks**: Prevent empty or null values
- **Duplicate Prevention**: Check for existing IDs before creation
- **Confirmation Prompts**: Require confirmation for destructive operations

---

## 6. User Workflow

### 6.1 First-Time Setup
1. Run the application
2. Select "Admin Signup"
3. Create administrator account
4. Login with admin credentials

### 6.2 Daily Operations (Admin/Staff)
1. Login with credentials
2. Select operation from menu
3. Perform CRUD operations on records
4. Logout when complete

### 6.3 Guest Access
1. Select "Guest Login"
2. View all available records
3. Logout

---

## 7. Implementation Details

### 7.1 Key Algorithms

#### Password Hashing
```python
def hash_pass(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
```

#### Record Search
```python
def find_record(student_id: str, records: List[Dict]):
    for record in records:
        if record.get("id") == student_id:
            return record
    return None
```

### 7.2 Data Persistence Strategy
- **Lazy Loading**: Data loaded only when needed
- **Immediate Save**: Changes written immediately to prevent data loss
- **JSON Format**: Human-readable storage for easy debugging
- **Error Handling**: JSONDecodeError handled gracefully

---

## 8. Testing & Validation

### 8.1 Test Cases

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-01 | Create admin account | Admin user created successfully |
| TC-02 | Duplicate admin signup | Error: Admin already exists |
| TC-03 | Password mismatch | Error: Passwords do not match |
| TC-04 | Invalid login | Error: Invalid username or password |
| TC-05 | Create record as admin | Record added successfully |
| TC-06 | Create record as guest | Access denied |
| TC-07 | View records as guest | Records displayed |
| TC-08 | Delete all as staff | Access denied |
| TC-09 | Update existing record | Record updated successfully |
| TC-10 | Delete non-existent record | Record not found |

---

## 9. Advantages

1. **Secure Authentication**: Industry-standard bcrypt password hashing
2. **Role-Based Access**: Granular control over user permissions
3. **No External Database**: Simple JSON-based storage
4. **Easy Deployment**: No server setup required
5. **User-Friendly**: Menu-driven interface
6. **Audit Trail**: Records track creator and timestamp
7. **Data Validation**: Prevents invalid or duplicate entries
8. **Confirmation Prompts**: Prevents accidental deletions

---

## 10. Limitations & Future Enhancements

### 10.1 Current Limitations
1. Single admin restriction (only one admin allowed)
2. No password recovery mechanism
3. No data export functionality
4. No search by name/course (only by ID)
5. No record modification history
6. No multi-user concurrent access handling

### 10.2 Future Enhancements
1. **Multiple Admin Support**: Allow multiple administrators
2. **Password Reset**: Email-based password recovery
3. **Advanced Search**: Filter by name, course, grade, date range
4. **Data Export**: CSV/Excel export functionality
5. **Backup & Restore**: Automated backup system
6. **Audit Logs**: Track all user actions
7. **Database Integration**: Migrate to SQLite/PostgreSQL
8. **Web Interface**: Flask/Django web application
9. **Reporting**: Generate statistical reports and analytics
10. **Email Notifications**: Alert administrators of important events

---

## 11. System Requirements

### 11.1 Software Requirements
- Python 3.7 or higher
- bcrypt library (install via `pip install bcrypt`)
- Operating System: Windows/Linux/macOS

### 11.2 Hardware Requirements
- Processor: Any modern CPU
- RAM: 256 MB minimum
- Storage: 10 MB for application and data

---

## 12. Installation & Usage

### 12.1 Installation Steps
```bash
# Clone or download the project
cd SRMS

# Install dependencies
pip install bcrypt

# Run the application
python auth.py
```

### 12.2 First Run
1. Select option 1 to create admin account
2. Enter admin username and password
3. Login with admin credentials
4. Start managing records

---

## 13. Code Statistics

- **Total Lines of Code**: ~380 lines
- **Functions**: 23
- **Classes**: 0 (Functional programming approach)
- **Files**: 1 main file (auth.py)
- **External Dependencies**: 1 (bcrypt)

---

## 14. Conclusion

The Student Record Management System successfully implements a secure, role-based application for managing student academic records. The system provides essential CRUD operations with proper authentication and authorization mechanisms. The use of bcrypt for password security and JSON for data persistence makes it a reliable solution for small to medium-scale educational institutions.

The modular design and clear separation of concerns make the codebase maintainable and extensible. While there are opportunities for enhancement, the current implementation fulfills the core requirements of a student record management system.

---

## 15. References

1. **Bcrypt Documentation**: https://pypi.org/project/bcrypt/
2. **Python JSON Module**: https://docs.python.org/3/library/json.html
3. **Python Type Hints**: https://docs.python.org/3/library/typing.html
4. **Password Hashing Best Practices**: OWASP Guidelines

---

**Project Developed By**: [Your Name]  
**Date**: December 2025  
**Version**: 1.0  
**Language**: Python 3.x  
**License**: [Specify if applicable]

---

*End of Report*
