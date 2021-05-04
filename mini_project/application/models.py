from application import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    complete = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)