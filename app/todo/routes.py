from flask import Blueprint, render_template, request, redirect, url_for


todo_bp = Blueprint('todolist', __name__)


@todo_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('pages/index.html')