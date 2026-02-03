from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import check_password_hash
from utils.db import get_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['role'] = user['role']

            if user['role'] == 'admin':
                return redirect('/admin/dashboard')
            else:
                return redirect('/teacher/dashboard')

        return "Invalid Credentials"

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')