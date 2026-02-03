from flask import Blueprint, render_template, request, redirect
from utils.decorators import role_required
from utils.db import get_connection
from werkzeug.security import generate_password_hash

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@role_required('admin')
def dashboard():
    return render_template('dashboard.html')


@admin_bp.route('/manage-teachers', methods=['GET', 'POST'])
@role_required('admin')
def manage_teachers():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, 'teacher')",
            (name, email, password)
        )
        conn.commit()

    cursor.execute("SELECT id, name, email FROM users WHERE role='teacher'")
    teachers = cursor.fetchall()

    conn.close()
    return render_template('manage_teachers.html', teachers=teachers)


@admin_bp.route('/manage-students', methods=['GET', 'POST'])
@role_required('admin')
def manage_students():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        class_name = request.form['class']

        cursor.execute(
            "INSERT INTO students (name, roll_no, class) VALUES (%s, %s, %s)",
            (name, roll_no, class_name)
        )
        conn.commit()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return render_template('manage_students.html', students=students)


@admin_bp.route('/assign-students', methods=['GET', 'POST'])
@role_required('admin')
def assign_students():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        student_id = request.form['student_id']

        cursor.execute(
            "INSERT IGNORE INTO teacher_student_map (teacher_id, student_id) VALUES (%s, %s)",
            (teacher_id, student_id)
        )
        conn.commit()

    cursor.execute("SELECT id, name FROM users WHERE role='teacher'")
    teachers = cursor.fetchall()

    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()

    conn.close()
    return render_template(
        'assign_students.html',
        teachers=teachers,
        students=students
    )



@admin_bp.route('/attendance-report')
@role_required('admin')
def attendance_report():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            s.name AS student_name,
            a.date,
            a.status,
            u.name AS teacher_name
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        JOIN users u ON a.marked_by = u.id
        ORDER BY a.date DESC
    """)

    records = cursor.fetchall()
    conn.close()

    return render_template(
        'attendance_report.html',
        records=records,
        role='admin'
    )