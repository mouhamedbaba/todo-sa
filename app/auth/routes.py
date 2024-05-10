from flask import Blueprint, session,request, redirect, url_for, render_template
from app.lib.postgres import Postgres
auth_bp = Blueprint('auth', __name__)

postges = Postgres()

@auth_bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'POST':
        user = request.form.to_dict()
        print(user)
        user = postges.get_user_by_username_and_password(username=user['username'], password=user['password'])
        if user:
            session['user'] = user
            return redirect(url_for('todolist.index'))
        else:
            return render_template('pages/auth/login.html', error='Invalid username or password')

    return render_template('pages/auth/login.html')

@auth_bp.route('/logout', methods=['GET', 'POST'], endpoint='logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))