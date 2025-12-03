''''
import json
import os
from datetime import datetime


class RecordManager:
    def __init__(self, filename="records.json"):
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_records(self):
        with open(self.filename, "w") as f:
            json.dump(self.records, f, indent=4)

    def add_record(self, student_id, name, course, grade):
        record = {
            "id": student_id,
            "name": name,
            "course": course,
            "grade": grade,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.records.append(record)
        self.save_records()
        print(f" Record added successfully for {name}")

    def view_all_records(self):
        if not self.records:
            print("\nNo records found.")
            return
        
        print(f"\n{'ID':<10} {'Name':<20} {'Course':<15} {'Grade':<10} {'Created':<20}")
        print("-" * 75)
        for record in self.records:
            print(
                f"{record['id']:<10} {record['name']:<20} {record['course']:<15} "
                f"{record['grade']:<10} {record['created_at']:<20}"
            )

    def search_record(self, student_id):
        for record in self.records:
            if record["id"] == student_id:
                print(f"ID: {record['id']}")
                print(f"Name: {record['name']}")
                print(f"Course: {record['course']}")
                print(f"Grade: {record['grade']}")
                print(f"Created: {record['created_at']}")
                return record
        print(f"\nRecord with ID '{student_id}' not found.")
        return None

    def update_record(self, student_id, name=None, course=None, grade=None):
        for record in self.records:
            if record["id"] == student_id:
                if name:
                    record["name"] = name
                if course:
                    record["course"] = course
                if grade:
                    record["grade"] = grade
                self.save_records()
                print(f" Record updated successfully for ID: {student_id}")
                return True
        print(f"\nRecord with ID '{student_id}' not found.")
        return False

    def delete_record(self, student_id):
        for i, record in enumerate(self.records):
            if record["id"] == student_id:
                deleted = self.records.pop(i)
                self.save_records()
                print(f" Record deleted successfully for {deleted['name']}")
                return True
        print(f"\nRecord with ID '{student_id}' not found.")
        return False

    def delete_all_records(self):
        self.records = []
        self.save_records()
        print("All records deleted successfully.")
        return True


def display_menu():
    print("\n  STUDENT RECORD MANAGEMENT SYSTEM")
    print("1. Add New Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Delete All Records")
    print("7. Exit")

def main():
    manager = RecordManager()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            print("\n   Add New Record    ")
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            course = input("Enter Course: ").strip()
            grade = input("Enter Grade: ").strip()
            manager.add_record(student_id, name, course, grade)

        elif choice == "2":
            manager.view_all_records()

        elif choice == "3":
            print("\n   Search Record    ")
            student_id = input("Enter Student ID to search: ").strip()
            manager.search_record(student_id)

        elif choice == "4":
            print("\n    Update Record    ")
            student_id = input("Enter Student ID to update: ").strip()
            if manager.search_record(student_id):
                name = input("Enter new Name (or press Enter to skip): ").strip()
                course = input("Enter new Course (or press Enter to skip): ").strip()
                grade = input("Enter new Grade (or press Enter to skip): ").strip()
                manager.update_record(
                    student_id,
                    name if name else None,
                    course if course else None,
                    grade if grade else None,
                )

        elif choice == "5":
            print("\n    Delete Record    ")
            student_id = input("Enter Student ID to delete: ").strip()
            confirm = (
                input(f"Are you sure you want to delete record '{student_id}'? (y/n): ").strip().lower()
            )
            if confirm == "y":
                manager.delete_record(student_id)
            else:
                print("Deletion cancelled.")

        elif choice == "6":
            print("\n    Delete All Records    ")
            confirm = (
                input("Are you sure you want to delete all records? (y/n): ")
                .strip()
                .lower()
            )
            if confirm == "y":
                manager.delete_all_records()
            else:
                print("Deletion cancelled.")

        elif choice == "7":
            print("\nThank you for using SRMS!")
            break

        else:
            print("\n Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
'''