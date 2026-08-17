import pymysql
import os
from dotenv import load_dotenv

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


# Get a valid GPA
def get_valid_gpa():
    while True:
        try:
            gpa = float(input("Enter GPA (0.0 - 5.0): "))

            if 0.0 <= gpa <= 5.0:
                return gpa

            print("Invalid GPA. Please enter a value between 0.0 and 5.0.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# View all students
def view_students():
    try:
        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()

        print("\n--- Students ---")

        if not students:
            print("No students found.")
            return

        for student in students:
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Major: {student[2]}")
            print(f"GPA: {student[3]}")
            print("-" * 30)

    except pymysql.Error as error:
        print("Database error:", error)


# Add a student
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ").strip()
        major = input("Enter Major: ").strip()

        if not name or not major:
            print("Name and major cannot be empty.")
            return

        gpa = get_valid_gpa()

        sql = """
        INSERT INTO Students (student_id, name, major, gpa)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (student_id, name, major, gpa))
        connection.commit()

        print("Student added successfully!")

    except ValueError:
        print("Student ID must be a number.")

    except pymysql.Error as error:
        connection.rollback()
        print("Database error:", error)


# Search for a student
def search_student():
    try:
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

    except ValueError:
        print("Student ID must be a number.")

    except pymysql.Error as error:
        print("Database error:", error)


# Update a student
def update_student():
    try:
        student_id = int(input("Enter Student ID to update: "))

        new_name = input("Enter new name: ").strip()
        new_major = input("Enter new major: ").strip()

        if not new_name or not new_major:
            print("Name and major cannot be empty.")
            return

        new_gpa = get_valid_gpa()

        sql = """
        UPDATE Students
        SET name = %s, major = %s, gpa = %s
        WHERE student_id = %s
        """

        cursor.execute(
            sql,
            (new_name, new_major, new_gpa, student_id)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Student ID must be a number.")

    except pymysql.Error as error:
        connection.rollback()
        print("Database error:", error)


# Delete a student
def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: "))

        # Check if student exists
        cursor.execute(
            "SELECT * FROM Students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        confirm = input(
f"Are you sure you want to delete {student[1]}? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            cursor.execute(
                "DELETE FROM Students WHERE student_id = %s",
                (student_id,)
            )

            connection.commit()

            print("Student deleted successfully!")

        else:
            print("Delete cancelled.")

    except ValueError:
        print("Student ID must be a number.")

    except pymysql.Error as error:
        connection.rollback()
        print("Database error:", error)


# Main menu
while True:

    print("\n===== Student Management System =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

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
        print("Invalid choice. Please choose 1-6.")


# Close connection
cursor.close()
connection.close()