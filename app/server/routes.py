from . import SERVER_BLUEPRINT
from db.database import ToDo
from run import db
from flask import render_template, request, redirect, url_for


@SERVER_BLUEPRINT.route('/')
def index():
    todo_list = ToDo.query.all()
    return render_template('index.html', todo_list=todo_list)


@SERVER_BLUEPRINT.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_todo = ToDo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@SERVER_BLUEPRINT.route('/update/<int:todo_id_task>')
def update(todo_id_task):
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))


@SERVER_BLUEPRINT.route('/delete/<int:todo_id_task>')
def delete(todo_id_task):
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
