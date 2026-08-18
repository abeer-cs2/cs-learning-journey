Student Management System
A simple Student Management System built with Python and MySQL.
The system allows users to manage student records through a command-line interface.
Features
View all students
Add a new student
Search for a student
Update student information
Delete a student
Store student data in a MySQL database
Use environment variables to protect database credentials
Technologies Used
Python
MySQL
MySQL Workbench
mysql-connector-python
python-dotenv
Git & GitHub
Database
The project uses a MySQL database named:
student_management
The database contains the following tables:
Students
Stores student information:
student_id
name
major
gpa
Courses
Stores course information:
course_id
course_name
Enrollments
Stores student course enrollments:
student_id
course_id
grade
Project Structure
student-management-system/
│
├── main.py
├── database.py
├── student_operations.py
├── database.sql
├── queries.sql
├── requirements.txt
├── README.md
├── .gitignore
└── .env
The .env file contains private database credentials and should not be uploaded to GitHub.
Setup
1. Clone the repository
git clone <your-repository-url>
2. Open the project folder
cd student-management-system
3. Install the required packages
pip install -r requirements.txt
4. Create the database
Open MySQL Workbench and run the SQL commands in:
database.sql
5. Configure the environment variables
Create a .env file in the project folder and add your own database information:
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=student_management
Do not share your actual password or upload the .env file to GitHub.
6. Run the application
python main.py
How to Use
After running the program, the main menu will appear:
===== Student Management System =====
1. View Students
2. Add Student
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Choose the number of the operation you want to perform and follow the instructions shown on the screen.
Security
Database credentials are stored in environment variables using a .env file instead of being written directly inside the Python code.
The .env file is excluded from Git using .gitignore.
Author
Student Management System Project