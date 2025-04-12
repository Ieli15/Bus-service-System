from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User

def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user = User.query.get(get_jwt_identity())
        if not user or user.role != 'admin':
            return {"message": "Admin access required"}, 403
        return fn(*args, **kwargs)
    return wrapper
