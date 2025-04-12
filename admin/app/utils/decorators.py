from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from flask import jsonify
from app.models.user import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if user and user.role == 'admin':
            return fn(*args, **kwargs)
        return jsonify({"msg": "Admins only"}), 403
    return wrapper
