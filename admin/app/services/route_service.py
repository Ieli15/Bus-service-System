from app.models.route import Route
from app import db

def create_route(data):
    route = Route(**data)
    db.session.add(route)
    db.session.commit()
    return route

def update_route(route_id, data):
    route = Route.query.get(route_id)
    if not route:
        return None
    for key, value in data.items():
        setattr(route, key, value)
    db.session.commit()
    return route

def delete_route(route_id):
    route = Route.query.get(route_id)
    if not route:
        return None
    db.session.delete(route)
    db.session.commit()
    return True

def get_all_routes():
    return Route.query.all()
