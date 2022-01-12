from flask import render_template, request, redirect, url_for

from app.db.models import ToDo, DB
from . import SERVER_BLUEPRINT


@SERVER_BLUEPRINT.route("/")
def index():
    """
    Presents the whole To-Do List.
    :return:
    :rtype:
    """
    todo_list = ToDo.query.all()
    return render_template(
        "index.html", todo_list=todo_list)


@SERVER_BLUEPRINT.route("/add", methods=["POST"])
def add():
    """
    Adds a new task to To-Do List (to table 'Today').
    """
    title = request.form.get("title")
    priority = request.form.get("priority")
    new_todo = ToDo(title=title, complete=False, when="Today", priority=priority)
    DB.session.add(new_todo)
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/update/<int:todo_id_task>")
def update(todo_id_task):
    """
    Changes the task's status (from 'To-Do' to 'Done' and conversely).
    :param todo_id_task: ID of the task
    :type todo_id_task: int
    """
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    todo.complete = not todo.complete
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/delete/<int:todo_id_task>")
def delete(todo_id_task):
    """
    Deletes the task.
    :param todo_id_task: ID of the task
    :type todo_id_task: int
    """
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    DB.session.delete(todo)
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/move/<str:when>/<int:todo_id_task>")
def move(when, todo_id_task):
    """
    Moves the task to another table.
    :param when: table where you want to move the task
    :type when: str
    :param todo_id_task: ID of the task
    :type todo_id_task: int
    """
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    todo.when = when
    DB.session.commit()
    return redirect(url_for(".index"))

