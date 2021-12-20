from flask import render_template, request, redirect, url_for

from app.db.models import ToDo, ThisWeek, NextWeek, DB
from . import SERVER_BLUEPRINT


@SERVER_BLUEPRINT.route("/")
def index():
    todo_list = ToDo.query.all()
    this_week = ThisWeek.query.all()
    next_week = NextWeek.query.all()
    return render_template("index.html", todo_list=todo_list, this_week=this_week, next_week=next_week)


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


@SERVER_BLUEPRINT.route("/move/<int:todo_id_task>")
def move(todo_id_task):
    todo = ToDo.query.filter_by(id_task=todo_id_task).first()
    DB.session.delete(todo)
    new_todo = ThisWeek(title=todo.title, complete=todo.complete)
    DB.session.add(new_todo)
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/next_week/<int:todo_id_task>")
def move_to_next_week(todo_id_task):
    todo = ThisWeek.query.filter_by(id_task=todo_id_task).first()
    DB.session.delete(todo)
    new_todo = NextWeek(title=todo.title, complete=todo.complete)
    DB.session.add(new_todo)
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/previous_week/<int:todo_id_task>")
def move_to_previous_week(todo_id_task):
    todo = NextWeek.query.filter_by(id_task=todo_id_task).first()
    DB.session.delete(todo)
    new_todo = ThisWeek(title=todo.title, complete=todo.complete)
    DB.session.add(new_todo)
    DB.session.commit()
    return redirect(url_for(".index"))