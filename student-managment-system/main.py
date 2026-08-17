from student_operations import (
    view_students,
    add_student,
    search_student,
    update_student,
    delete_student
)


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