from flask import Flask

from .config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)

from app.todo.routes import todo_bp
from app.auth.routes import auth_bp
app.register_blueprint(todo_bp)
app.register_blueprint(auth_bp)
