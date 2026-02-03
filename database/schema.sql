CREATE DATABASE attendance_tracker;
USE attendance_tracker;

-- USERS (Admin / Teacher)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role ENUM('admin', 'teacher')
);

-- STUDENTS
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(50),
    class VARCHAR(50)
);

-- TEACHER-STUDENT MAPPING
CREATE TABLE teacher_student_map (
    teacher_id INT,
    student_id INT,
    PRIMARY KEY (teacher_id, student_id),
    FOREIGN KEY (teacher_id) REFERENCES users(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- ATTENDANCE
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    status ENUM('Present', 'Absent'),
    marked_by INT,
    UNIQUE(student_id, date),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (marked_by) REFERENCES users(id)
);