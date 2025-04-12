from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

# Registration Route (POST /auth/register)
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Check if the user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "User already exists."}), 400
    
    user = User(name=data['name'], email=data['email'])
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

# Login Route (POST /auth/login)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        # Create JWT token
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials."}), 401
