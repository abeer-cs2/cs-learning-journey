from database import get_connection


def get_valid_gpa():
    while True:
        try:
            gpa = float(input("Enter GPA (0.0 - 5.0): "))

            if 0.0 <= gpa <= 5.0:
                return gpa

            print("Invalid GPA. Please enter a value between 0.0 and 5.0.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def view_students():
    connection = get_connection()
    cursor = connection.cursor()

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

    except Exception as error:
        print("Database error:", error)

    finally:
        cursor.close()
        connection.close()


def add_student():
    connection = get_connection()
    cursor = connection.cursor()

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

    except Exception as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        cursor.close()
        connection.close()


def search_student():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        student_id = int(input("Enter Student ID to search: "))

        cursor.execute(
            "SELECT * FROM Students WHERE student_id = %s",
            (student_id,)
        )

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

    except Exception as error:
        print("Database error:", error)

    finally:
        cursor.close()
        connection.close()


def update_student():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        student_id = int(input("Enter Student ID to update: "))

        cursor.execute(
            "SELECT * FROM Students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        print(f"Current Name: {student[1]}")
        print(f"Current Major: {student[2]}")
        print(f"Current GPA: {student[3]}")

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

        print("Student updated successfully!")

    except ValueError:
        print("Student ID must be a number.")

    except Exception as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        cursor.close()
        connection.close()
def delete_student():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        student_id = int(input("Enter Student ID to delete: "))

        cursor.execute(
            "SELECT * FROM Students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        print(f"Student: {student[1]}")
        print(f"Major: {student[2]}")
        print(f"GPA: {student[3]}")

        confirm = input(
            "Are you sure you want to delete this student? (yes/no): "
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

    except Exception as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        cursor.close()
        connection.close()