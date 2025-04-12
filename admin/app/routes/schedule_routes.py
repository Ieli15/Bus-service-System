from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.schemas.schedule_schema import ScheduleSchema
from app.services import schedule_service

schedule_bp = Blueprint("schedule_bp", __name__)
schedule_schema = ScheduleSchema()
schedule_list_schema = ScheduleSchema(many=True)

@schedule_bp.route("/", methods=["POST"])
@jwt_required()
def add_schedule():
    data = request.get_json()
    schedule = schedule_service.create_schedule(data)
    return schedule_schema.dump(schedule), 201

@schedule_bp.route("/", methods=["GET"])
@jwt_required()
def list_schedules():
    schedules = schedule_service.get_schedules()
    return schedule_list_schema.dump(schedules), 200

@schedule_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def edit_schedule(id):
    data = request.get_json()
    schedule = schedule_service.update_schedule(id, data)
    return schedule_schema.dump(schedule), 200

@schedule_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_schedule(id):
    schedule_service.delete_schedule(id)
    return jsonify({"message": "Deleted successfully"}), 200
