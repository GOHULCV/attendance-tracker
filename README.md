📘 Attendance Tracker Web Application

A web-based Attendance Management System built using Flask, MySQL, HTML, and CSS, designed to help institutions efficiently manage students, teachers, and daily attendance with secure role-based access control.

⸻

🚀 Features

🔐 Authentication & Authorization
	•	Secure Login & Logout
	•	Password hashing using Werkzeug
	•	Session-based authentication
	•	Role-based access (Admin / Teacher)
	•	Route protection using decorators

⸻

👩‍💼 Admin Panel
	•	Add / Edit / Delete Teachers
	•	Add / Edit / Delete Students
	•	Assign students to teachers
	•	View attendance reports for all students
	•	Centralized dashboard with quick navigation

⸻

👨‍🏫 Teacher Panel
	•	View assigned students only
	•	Mark daily attendance (Present / Absent)
	•	Prevent duplicate attendance for the same date
	•	View attendance reports for assigned students
	•	Clean and focused teacher dashboard

⸻

📊 Attendance Management
	•	Date-wise attendance tracking
	•	Student-wise attendance reports
	•	Admin & Teacher specific views
	•	Visual status indicators (Present / Absent)
	•	Database-level data integrity using constraints

🧰 Tech Stack

Layer	Technology
Frontend	HTML, CSS
Backend	Python (Flask)
Database	MySQL
Security	Werkzeug (Password Hashing)
Version Control	Git & GitHub

📁 Project Folder Structure

attendance_tracker/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── routes/
│   ├── auth_routes.py
│   ├── admin_routes.py
│   ├── teacher_routes.py
│
├── utils/
│   ├── db.py
│   ├── decorators.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── teacher_dashboard.html
│   ├── manage_teachers.html
│   ├── manage_students.html
│   ├── assign_students.html
│   ├── mark_attendance.html
│   ├── attendance_report.html
│
├── static/
│   └── css/
│       ├── base.css
│       ├── login.css
│       ├── admin.css
│       ├── teacher.css
│       ├── manage_teachers.css
│       ├── manage_students.css
│       ├── assign_students.css
│       ├── mark_attendance.css
│       ├── attendance_report.css
│
├── screenshots/
│   ├── 1_login_page.png
│   ├── 2_admin_dashboard.png
│   ├── 3_manage_teachers.png
│   ├── 4_manage_students.png
│   ├── 5_assign_students.png
│   ├── 6_teacher_dashboard.png
│   ├── 7_mark_attendance.png
│   ├── 8_attendance_report.png

🗄️ Database Schema

Users Table

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password TEXT,
  role ENUM('admin','teacher')
);

Students Table

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  roll_no VARCHAR(50),
  class VARCHAR(50)
);

Teacher–Student Mapping

CREATE TABLE teacher_student_map (
  id INT AUTO_INCREMENT PRIMARY KEY,
  teacher_id INT,
  student_id INT
);

Attendance Table

CREATE TABLE attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT,
  date DATE,
  status ENUM('Present','Absent'),
  marked_by INT,
  UNIQUE(student_id, date)
);

⚙️ Setup Instructions

🔧 Installation & Setup

1.	Clone the repository

git clone https://github.com/GOHULCV/attendance-tracker.git

2.	Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

3.	Install dependencies

pip install -r requirements.txt

4.	Setup MySQL Database

•	Create database:
CREATE DATABASE attendance_tracker;

•	Run schema file in MySQL Workbench

5.	Run the application

python app.py

6.	Open in browser

http://127.0.0.1:5000

🔑 Default Login Credentials

👩‍💼 Admin
	•	Email: admin@example.com
	•	Password: admin123

👨‍🏫 Teacher
	•	Created by Admin via Manage Teachers
	•	Login using email & password set by Admin

	•	 Email : teacher@gmail.com
	•	Password: teacher123

🔒 Security Notes
	•	All passwords are securely hashed
	•	Unauthorized access is restricted using decorators
	•	Teachers can access only assigned student data
	•	Attendance duplication is prevented at database level

🖼️ Screenshots

Screenshots of the application UI are available in the screenshots/ folder, including:
	•	Login Page
	•	Admin Dashboard
	•	Manage Teachers
	•	Manage Students
	•	Assign Students
	•	Teacher Dashboard
	•	Mark Attendance
	•	Attendance Reports

🌱 Future Enhancements

	•	Search & filter attendance by date/class
	•	Email notifications
	•	Deployment to cloud (Render)