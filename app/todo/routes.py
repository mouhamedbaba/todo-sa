from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
import datetime
import random

from app.lib.postgres import Postgres

todo_bp = Blueprint('todolist', __name__)
postgres = Postgres()


@todo_bp.route('/', methods=['GET'], endpoint='index')
def index():
    if not session.get('user'):
        return redirect(url_for('auth.login'))
    return render_template('pages/index.html')



@todo_bp.route('/api/todos', methods=['GET'])
def todos():
    user = session.get('user')
    if not user:
        return jsonify({"error": "Unauthorized"}),403
    uid = user['uid']
    tasks = postgres.get_tasks(uid)
    return jsonify(tasks) if tasks else jsonify([])

@todo_bp.route('/api/todos', methods=['DELETE'])
def delete():
    try :
        user = session.get('user')
        if not user:
            return jsonify({"error": "Unauthorized"}),403
        t_id = request.json.get('id')
        postgres.delete_task(t_id)
        return jsonify({}), 200
    except Exception as e:
        return jsonify({"error": str(e)}),500
    
@todo_bp.route('/api/todos', methods=['UPDATE'])
def update():
    try :
        user = session.get('user')
        if not user:
            return jsonify({"error": "Unauthorized"}),403
        t_id = request.json.get('id')
        column = request.json.get('column')
        value = request.json.get('value')
        postgres.update_task(t_id, column, value)
        return jsonify({}), 200
    except Exception as e:
        return jsonify({"error": str(e)}),500
    
@todo_bp.route('/api/todos', methods=['POST'])
def add_task():
    try :
        user = session.get('user')
        if not user:
            return jsonify({"error": "Unauthorized"}),403
        uid = user['uid']
        priority = request.json.get('priority')
        if (priority == 'low'):
            head_color = '#5bbd75'
        elif (priority == 'medium'):
            head_color = 'orange'
        else:
            head_color = 'red'
        task = {
            'uid': uid,
            'title': request.json.get('title'),
            'priority': priority,
            'head_color': head_color,
            'deadline': request.json.get('deadline'),
            
        }
        
        postgres.create_task(**task)
        return jsonify(task), 201
    except Exception as e:
        return jsonify({"error": str(e)}),500
    
    
