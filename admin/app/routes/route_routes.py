from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.utils.decorators import admin_required
from app.schemas.route_schema import RouteSchema
from app.services import route_service

bp = Blueprint("routes", __name__, url_prefix="/admin/routes")

route_schema = RouteSchema()
route_list_schema = RouteSchema(many=True)

@bp.route("/", methods=["POST"])
@admin_required
def add_route():
    data = request.get_json()
    errors = route_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    route = route_service.create_route(data)
    return route_schema.dump(route), 201

@bp.route("/<int:route_id>", methods=["PUT"])
@admin_required
def edit_route(route_id):
    data = request.get_json()
    errors = route_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    route = route_service.update_route(route_id, data)
    if not route:
        return {"message": "Route not found"}, 404
    return route_schema.dump(route), 200

@bp.route("/<int:route_id>", methods=["DELETE"])
@admin_required
def remove_route(route_id):
    success = route_service.delete_route(route_id)
    if not success:
        return {"message": "Route not found"}, 404
    return {"message": "Route deleted"}, 200

@bp.route("/", methods=["GET"])
@jwt_required()
def list_routes():
    routes = route_service.get_all_routes()
    return route_list_schema.dump(routes), 200
