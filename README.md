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

1️⃣ Clone the Project
bash

git clone <repository-url>
cd attendance_tracker

2️⃣ Create Virtual Environment (Optional)
bash

python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
bash

pip install -r requirements.txt

4️⃣ Configure Database

edit config.py:

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'attendance_tracker'
SECRET_KEY = 'your_secret_key'

5️⃣ Create Database & Tables

Create database and run the SQL schemas above.

6️⃣ Create Admin User (Hashed Password)
bash

python
_____________________________________________________________________________________________
python

from werkzeug.security import generate_password_hash
print(generate_password_hash("admin123"))

Insert into MySQL:

INSERT INTO users (name, email, password, role)
VALUES ('Admin', 'admin@example.com', '<PASTE_HASH>', 'admin');

7️⃣ Run the Application
bash 

python app.py

Open in browser:
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