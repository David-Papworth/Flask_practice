from application import app, db
from application.models import Task

@app.route('/add')
def add():
    new_task = Task(description="New task added", complete=False)
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"

@app.route('/read')
def read():
    all_tasks = Task.query.all()
    task_string = ""
    for tas in all_tasks:
        task_string += "<br>"+ tas.description
    return task_string

@app.route('/update/<name>')
def update(name):
    first_task = Task.query.first()
    first_task.description = name
    db.session.commit()
    return first_task.description

@app.route('/delete')
def delete():
    first_task = Task.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "Deleted the first task"

@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.filter_by(id=id).first()
    task.complete = True
    db.session.commit()
    return f"The {id} task is complete"

@app.route('/incomplete/<int:id>')
def incomplete(id):
    task = Task.query.filter_by(id=id).first()
    task.complete = False
    db.session.commit()
    return f"The {id} task is incomplete"