import json
import os
import bcrypt
from datetime import datetime
from typing import List, Dict



USER_FILE = "users.json"
RECORDS_FILE = "records.json"


def read_json_file(path: str):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_json_file(path: str, data: list):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def find_user(username: str, users: List[Dict]):
    for user in users:
        if user.get("username") == username:
            return user
    return None


def hash_pass(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_pass(password: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except ValueError:
        return False


def enter_password():
    password = input("Enter password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return None

    confirm_password = input("Confirm password: ").strip()
    if password != confirm_password:
        print("Passwords do not match.")
        return None

    return password



def admin_signup():
    users = read_json_file(USER_FILE)

    if any(user.get("role") == "admin" for user in users):
        print("Admin already exists.")
        return False

    username = input("Enter admin username: ").strip()
    if not username:
        print("Enter a username")
        return False

    if find_user(username, users):
        print("Username already exists.")
        return False

    password = enter_password()
    if password is None:
        return False

    users.append({
        "username": username,
        "password": hash_pass(password),
        "role": "admin"
    })

    save_json_file(USER_FILE, users)
    print("Admin user created successfully.")
    return True


def staff_signup():
    users = read_json_file(USER_FILE)

    username = input("Enter staff username: ").strip()
    if not username:
        print("Enter a username")
        return False

    if find_user(username, users):
        print("Username already exists.")
        return False

    password = enter_password()
    if password is None:
        return False

    users.append({
        "username": username,
        "password": hash_pass(password),
        "role": "staff"
    })

    save_json_file(USER_FILE, users)
    print("Staff user created successfully.")
    return True


def guest_login() -> Dict:
    print("Logging in as guest...")
    return {
        "username": "guest",
        "role": "guest"
    }


def login() -> Dict | None:
    users = read_json_file(USER_FILE)

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    user = find_user(username, users)
    if user is None:
        print("Invalid username or password.")
        return None

    if not verify_pass(password, user.get("password", "")):
        print("Invalid username or password.")
        return None

    print(f"Login successful. Welcome {username}!")
    return user




def read_records():
    return read_json_file(RECORDS_FILE)


def save_records(records: List[Dict]):
    save_json_file(RECORDS_FILE, records)


def find_record(student_id: str, records: List[Dict]):
    for record in records:
        if record.get("id") == student_id:
            return record
    return None


def create_record(user: Dict):
    if user.get("role") not in ["admin", "staff"]:
        print("Access denied. Only admin and staff can create records.")
        return False

    records = read_records()
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return False

    if find_record(student_id, records):
        print(f"Record with ID '{student_id}' already exists.")
        return False

    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()
    grade = input("Enter Grade: ").strip()

    if not name or not course or not grade:
        print("All fields are required.")
        return False

    record = {
        "id": student_id,
        "name": name,
        "course": course,
        "grade": grade,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "created_by": user.get("username")
    }

    records.append(record)
    save_records(records)
    print(f"Record added successfully for {name}.")
    return True


def view_all_records(user: Dict):
    records = read_records()
    if not records:
        print("\nNo records found.")
        return True

    print(f"\n{'ID':<10} {'Name':<20} {'Course':<15} {'Grade':<10} {'Created':<20}")
    print("-" * 75)
    for record in records:
        print(
            f"{record['id']:<10} {record['name']:<20} {record['course']:<15} "
            f"{record['grade']:<10} {record['created_at']:<20}"
        )
    return True


def search_record(user: Dict):
    if user.get("role") not in ["admin", "staff"]:
        print("Access denied. Only admin and staff can search records.")
        return False

    records = read_records()
    student_id = input("Enter Student ID to search: ").strip()

    record = find_record(student_id, records)
    if record is None:
        print(f"\nRecord with ID '{student_id}' not found.")
        return False

    print(f"\nID: {record['id']}")
    print(f"Name: {record['name']}")
    print(f"Course: {record['course']}")
    print(f"Grade: {record['grade']}")
    print(f"Created: {record['created_at']}")
    print(f"Created by: {record.get('created_by', 'N/A')}")
    return True


def update_record(user: Dict):
    if user.get("role") not in ["admin", "staff"]:
        print("Access denied. Only admin and staff can update records.")
        return False

    records = read_records()
    student_id = input("Enter Student ID to update: ").strip()

    record = find_record(student_id, records)
    if record is None:
        print(f"\nRecord with ID '{student_id}' not found.")
        return False

    print(f"\nCurrent record details:")
    print(f"Name: {record['name']}")
    print(f"Course: {record['course']}")
    print(f"Grade: {record['grade']}")

    name = input("Enter new Name (or press Enter to skip): ").strip()
    course = input("Enter new Course (or press Enter to skip): ").strip()
    grade = input("Enter new Grade (or press Enter to skip): ").strip()

    if name:
        record["name"] = name
    if course:
        record["course"] = course
    if grade:
        record["grade"] = grade

    save_records(records)
    print(f"Record updated successfully for ID: {student_id}.")
    return True


def delete_record(user: Dict):
    if user.get("role") not in ["admin", "staff"]:
        print("Access denied. Only admin and staff can delete records.")
        return False

    records = read_records()
    student_id = input("Enter Student ID to delete: ").strip()

    record = find_record(student_id, records)
    if record is None:
        print(f"\nRecord with ID '{student_id}' not found.")
        return False

    confirm = input(f"Are you sure you want to delete record for '{record['name']}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return False

    records = [r for r in records if r.get("id") != student_id]
    save_records(records)
    print(f"Record deleted successfully for {record['name']}.")
    return True


def delete_all_records(user: Dict):
    if user.get("role") != "admin":
        print("Access denied. Only admin can delete all records.")
        return False

    records = read_records()
    if not records:
        print("\nNo records to delete.")
        return True

    confirm = input(f"Are you sure you want to delete all {len(records)} records? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return False

    save_records([])
    print("All records deleted successfully.")
    return True



def view_all_users(user: Dict):
    if user.get("role") != "admin":
        print("Access denied. Only admin can view users.")
        return False
    
    users = read_json_file(USER_FILE)
    if not users:
        print("\nNo users found.")
        return True
    
    print(f"\n{'Username':<20} {'Role':<15}")
    print("-" * 35)
    for u in users:
        print(f"{u['username']:<20} {u['role']:<15}")
    return True


def delete_user(user: Dict):
    if user.get("role") != "admin":
        print("Access denied. Only admin can delete users.")
        return False
    
    users = read_json_file(USER_FILE)
    username = input("Enter username to delete: ").strip()
    
    target_user = find_user(username, users)
    if target_user is None:
        print(f"\nUser '{username}' not found.")
        return False
    
    if target_user.get("username") == user.get("username"):
        print("You cannot delete your own account.")
        return False
    
    if target_user.get("role") == "admin":
        admin_count = sum(1 for u in users if u.get("role") == "admin")
        if admin_count <= 1:
            print("Cannot delete the last admin account.")
            return False
    
    confirm = input(f"Are you sure you want to delete user '{username}' ({target_user.get('role')})? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return False
    
    users = [u for u in users if u.get("username") != username]
    save_json_file(USER_FILE, users)
    print(f"User '{username}' deleted successfully.")
    return True



def display_auth_menu():
    print("\n=== STUDENT RECORD MANAGEMENT SYSTEM ===")
    print("1. Admin Signup")
    print("2. Staff Signup")
    print("3. Login")
    print("4. Guest Login (View Only)")
    print("5. Exit")


def display_main_menu(user: Dict):
    print(f"\n=== SRMS - Welcome {user.get('username')} ({user.get('role')}) ===")

    if user.get("role") == "guest":
        print("1. View All Records")
        print("0. Logout")
    else:
        print("1. Create Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        if user.get("role") == "admin":
            print("6. Delete All Records (Admin Only)")
            print("7. View All Users (Admin Only)")
            print("8. Delete User (Admin Only)")
        print("0. Logout")


def main():
    current_user = None

    while True:
        if current_user is None:
            display_auth_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                admin_signup()
            elif choice == "2":
                staff_signup()
            elif choice == "3":
                current_user = login()
            elif choice == "4":
                current_user = guest_login()
            elif choice == "5":
                print("\nThank you for using SRMS!")
                break
            else:
                print("Invalid choice. Please try again.")

        else:
            display_main_menu(current_user)
            choice = input("\nEnter your choice: ").strip()

            if current_user.get("role") == "guest":
                if choice == "1":
                    view_all_records(current_user)
                elif choice == "0":
                    print(f"\nLogging out {current_user.get('username')}...")
                    current_user = None
                else:
                    print("Invalid choice. Please try again.")

            else:
                if choice == "1":
                    create_record(current_user)
                elif choice == "2":
                    view_all_records(current_user)
                elif choice == "3":
                    search_record(current_user)
                elif choice == "4":
                    update_record(current_user)
                elif choice == "5":
                    delete_record(current_user)
                elif choice == "6" and current_user.get("role") == "admin":
                    delete_all_records(current_user)
                elif choice == "7" and current_user.get("role") == "admin":
                    view_all_users(current_user)
                elif choice == "8" and current_user.get("role") == "admin":
                    delete_user(current_user)
                elif choice == "0":
                    print(f"\nLogging out {current_user.get('username')}...")
                    current_user = None
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
