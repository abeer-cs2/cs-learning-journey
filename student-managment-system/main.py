import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# Connect to MySQL
connection = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor()


# View all students
def view_students():
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()

    print("\n--- Students ---")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Major: {student[2]}")
        print(f"GPA: {student[3]}")
        print("-" * 30)


# Add a student
def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    major = input("Enter Major: ")
    gpa = float(input("Enter GPA: "))

    sql = """
    INSERT INTO Students (student_id, name, major, gpa)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (student_id, name, major, gpa))
    connection.commit()

    print("Student added successfully!")


# Search for a student
def search_student():
    student_id = int(input("Enter Student ID to search: "))

    sql = "SELECT * FROM Students WHERE student_id = %s"
    cursor.execute(sql, (student_id,))

    student = cursor.fetchone()

    if student:
        print("\n--- Student Found ---")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Major: {student[2]}")
        print(f"GPA: {student[3]}")
    else:
        print("Student not found.")


# Update a student
def update_student():
    student_id = int(input("Enter Student ID to update: "))

    new_name = input("Enter new name: ")
    new_major = input("Enter new major: ")
    new_gpa = float(input("Enter new GPA: "))

    sql = """
    UPDATE Students
    SET name = %s, major = %s, gpa = %s
    WHERE student_id = %s
    """

    cursor.execute(sql, (new_name, new_major, new_gpa, student_id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found.")


# Delete a student
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    sql = "DELETE FROM Students WHERE student_id = %s"

    cursor.execute(sql, (student_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main menu
while True:

    print("\n===== Student Management System =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


# Close connection
cursor.close()
connection.close()