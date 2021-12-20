from flask import render_template, request, redirect, url_for

from app.db.models import ToDo, ThisWeek, NextWeek, DB
from app.services.task_manger import filter_task, filter_tb
from . import SERVER_BLUEPRINT


@SERVER_BLUEPRINT.route("/")
def index():
    todo_list = ToDo.query.all()
    this_week = ThisWeek.query.all()
    next_week = NextWeek.query.all()
    return render_template(
        "index.html", todo_list=todo_list, this_week=this_week, next_week=next_week
    )


@SERVER_BLUEPRINT.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = ToDo(title=title, complete=False)
    DB.session.add(new_todo)
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/update/<class_name>/<int:todo_id_task>")
def update(class_name, todo_id_task):
    todo = filter_task(tb_key=class_name, todo_id_task=todo_id_task)
    todo.complete = not todo.complete
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/delete/<class_name>/<int:todo_id_task>")
def delete(class_name, todo_id_task):
    todo = filter_task(tb_key=class_name, todo_id_task=todo_id_task)
    DB.session.delete(todo)
    DB.session.commit()
    return redirect(url_for(".index"))


@SERVER_BLUEPRINT.route("/<move_from>/<move_to>/<int:todo_id_task>")
def move(move_from, move_to, todo_id_task):
    todo = filter_task(tb_key=move_from, todo_id_task=todo_id_task)
    DB.session.delete(todo)
    new_todo = filter_tb(tb_key=move_to)(title=todo.title, complete=todo.complete)
    DB.session.add(new_todo)
    DB.session.commit()
    return redirect(url_for(".index"))

