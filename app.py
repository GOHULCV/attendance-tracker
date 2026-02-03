from flask import Flask
from config import *

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Register routes
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.teacher_routes import teacher_bp

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(teacher_bp)

if __name__ == "__main__":
    app.run(debug=True)