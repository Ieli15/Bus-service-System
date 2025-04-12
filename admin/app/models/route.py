from app.extensions import db

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    schedules = db.relationship('Schedule', backref='route', lazy=True)
