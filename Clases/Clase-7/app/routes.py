from flask import Blueprint, render_template, redirect, url_for, request
from .models import Task
from .forms import TaskForm
from . import db

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("main.index"))

    tasks = Task.query.order_by(Task.id.desc()).all()
    return render_template("index.html", form=form, tasks=tasks)


@main.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("main.index"))


@main.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("main.index"))
