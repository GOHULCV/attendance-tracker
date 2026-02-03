from functools import wraps
from flask import session, redirect

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            if session.get('role') != role:
                return redirect('/')
            return fn(*args, **kwargs)
        return decorated
    return wrapper