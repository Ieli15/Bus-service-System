from app.extensions import db

class Bus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(20), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    operator = db.Column(db.String(100))
    schedules = db.relationship('Schedule', backref='bus', lazy=True)
