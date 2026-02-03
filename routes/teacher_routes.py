from flask import Blueprint, render_template, request
from utils.decorators import role_required
from utils.db import get_connection
from flask import session
from datetime import date

teacher_bp = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacher_bp.route('/dashboard')
@role_required('teacher')
def dashboard():
    return render_template('teacher_dashboard.html')

@teacher_bp.route('/mark-attendance', methods=['GET', 'POST'])
@role_required('teacher')
def mark_attendance():
    teacher_id = session['user_id']
    today = date.today()

    conn = get_connection()
    cursor = conn.cursor()

    # Get assigned students
    cursor.execute("""
        SELECT s.id, s.name
        FROM students s
        JOIN teacher_student_map tsm ON s.id = tsm.student_id
        WHERE tsm.teacher_id = %s
    """, (teacher_id,))
    students = cursor.fetchall()

    if request.method == 'POST':
        for student in students:
            status = request.form.get(str(student['id']))
            cursor.execute("""
                INSERT INTO attendance (student_id, date, status, marked_by)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE status=%s
            """, (student['id'], today, status, teacher_id, status))

        conn.commit()

    conn.close()
    return render_template(
        'mark_attendance.html',
        students=students,
        today=today
    )

@teacher_bp.route('/attendance-report')
@role_required('teacher')
def attendance_report():
    teacher_id = session['user_id']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            s.name AS student_name,
            a.date,
            a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        JOIN teacher_student_map tsm ON s.id = tsm.student_id
        WHERE tsm.teacher_id = %s
        ORDER BY a.date DESC
    """, (teacher_id,))

    records = cursor.fetchall()
    conn.close()

    return render_template(
        'attendance_report.html',
        records=records,
        role='teacher'
    )