from flask import render_template, request, redirect, url_for

from app.db.models import ToDo, DB
from . import SERVER_BLUEPRINT


@SERVER_BLUEPRINT.route("/")
def index():
    todo_list = ToDo.query.all()
    return render_template("index.html", todo_list=todo_list)


@SERVER_BLUEPRINT.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = ToDo(title=title, complete=False)
    DB.session.add(new_todo)
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/update/<int:todo_id_task>")
def update(todo_id_task):
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    todo.complete = not todo.complete
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/delete/<int:todo_id_task>")
def delete(todo_id_task):
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    DB.session.delete(todo)
    DB.session.commit()
    return redirect(url_for(".index"))
