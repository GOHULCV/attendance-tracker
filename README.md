📘 Attendance Tracker Web Application

A web-based Attendance Management System built using Flask, MySQL, and HTML, designed to help institutions manage students, teachers, and daily attendance with role-based access control.

⸻


🚀 Features:

🔐 Authentication & Authorization
	•	Secure Login & Logout
	•	Password hashing using Werkzeug
	•	Session-based authentication
	•	Role-based access (Admin / Teacher)

👩‍💼 Admin Panel
	•	Add / Edit / Delete Teachers
	•	Add / Edit / Delete Students
	•	Assign students to teachers
	•	View attendance reports for all students

👨‍🏫 Teacher Panel
	•	View assigned students
	•	Mark daily attendance (Present / Absent)
	•	Prevent duplicate attendance for the same date
	•	View attendance reports for assigned students only

📊 Attendance Management
	•	Date-wise attendance tracking
	•	Student-wise attendance report
	•	Admin & Teacher specific views
	•	Data integrity using database constraints


🧰 Tech Stack:

    Layer              Technology
    Frontend           HTML,CSS
    Backend            Python(flask)
    Database           MySQL
    Security           Werkzeug (Password Hashing)


📁 Project Folder Structure:

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
│   ├── login.html
│   ├── dashboard.html
│   ├── manage_teachers.html
│   ├── manage_students.html
│   ├── assign_students.html
│   ├── mark_attendance.html
│   ├── attendance_report.html
│   |__ teacher_dashboard.html
├── static/
│   └── style.css


🗄️ Database Schema:

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

Teacher-Student Mapping

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


⚙️ Setup Instructions:

## Installation & Setup

1. Clone the repository
   git clone https://github.com/GOHULCV/attendance-tracker.git

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Setup MySQL Database
   - Create database `attendance_tracker`
   - Run `database/schema.sql` in MySQL Workbench

5. Run the application
   python app.py

6. Open browser
   http://127.0.0.1:5000

🔑 Default Login: 

Admin

Email: admin@example.com
Password: admin123

Teacher

• Created by Admin via Manage Teachers
• Uses email & password set by Admin


🔒 Security Notes:

	•	All passwords are securely hashed
	•	Unauthorized access is restricted using decorators
	•	Teachers can access only assigned student data