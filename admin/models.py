# models.py
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default='user')

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_name = db.Column(db.String(100))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'), nullable=True)

    # Add these fields to avoid errors in /book route
    bus = db.Column(db.String(100))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
