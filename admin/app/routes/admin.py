from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.bus import Bus
from app.models.route import Route
from app.models.schedule import Schedule

admin_bp = Blueprint('admin', __name__)

# === BUSES ===
@admin_bp.route('/buses', methods=['POST'])
def add_bus():
    data = request.get_json()
    bus = Bus(**data)
    db.session.add(bus)
    db.session.commit()
    return jsonify({"message": "Bus added"}), 201

@admin_bp.route('/buses', methods=['GET'])
def get_buses():
    return jsonify([{"id": b.id, "number_plate": b.number_plate} for b in Bus.query.all()])

# === ROUTES ===
@admin_bp.route('/routes', methods=['POST'])
def add_route():
    data = request.get_json()
    route = Route(**data)
    db.session.add(route)
    db.session.commit()
    return jsonify({"message": "Route added"}), 201

# === SCHEDULES ===
@admin_bp.route('/schedules', methods=['POST'])
def add_schedule():
    data = request.get_json()
    schedule = Schedule(**data)
    db.session.add(schedule)
    db.session.commit()
    return jsonify({"message": "Schedule added"}), 201
