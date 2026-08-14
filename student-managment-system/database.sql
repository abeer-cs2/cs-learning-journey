CREATE DATABASE student_management;
USE student_management;
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    major VARCHAR(50),
    gpa DECIMAL(3,2)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    grade VARCHAR(2),

    PRIMARY KEY (student_id, course_id),

    FOREIGN KEY (student_id)
        REFERENCES Students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES Courses(course_id)
);


INSERT INTO Students (student_id, name, major, gpa)
VALUES
(1, 'Sara', 'CS', 4.20),
(2, 'Nora', 'CS', 3.80),
(3, 'Layan', 'IS', 4.50),
(4, 'Reem', 'CS', 3.60);


INSERT INTO Courses (course_id, course_name)
VALUES
(101, 'Database'),
(102, 'Data Structures'),
(103, 'Programming');


INSERT INTO Enrollments (student_id, course_id, grade)
VALUES
(1, 101, 'A'),
(1, 102, 'B+'),
(2, 101, 'A'),
(2, 103, 'A-'),
(3, 102, 'A'),
(4, 103, 'B');