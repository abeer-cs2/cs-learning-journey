USE student_management;

SELECT 
    Students.name,
    Courses.course_name,
    Enrollments.grade
FROM Enrollments
JOIN Students
    ON Enrollments.student_id = Students.student_id
JOIN Courses
    ON Enrollments.course_id = Courses.course_id;