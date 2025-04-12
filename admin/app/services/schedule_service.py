from app.models.schedule import Schedule
from app.extensions import db

def create_schedule(data):
    schedule = Schedule(**data)
    db.session.add(schedule)
    db.session.commit()
    return schedule

def get_schedules():
    return Schedule.query.all()

def get_schedule(schedule_id):
    return Schedule.query.get_or_404(schedule_id)

def update_schedule(schedule_id, data):
    schedule = get_schedule(schedule_id)
    for key, value in data.items():
        setattr(schedule, key, value)
    db.session.commit()
    return schedule

def delete_schedule(schedule_id):
    schedule = get_schedule(schedule_id)
    db.session.delete(schedule)
    db.session.commit()
