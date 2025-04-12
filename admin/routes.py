# routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from extensions import db
from models import User, Booking
from werkzeug.security import generate_password_hash, check_password_hash

# Create the blueprint for routes
api_routes = Blueprint('api_routes', __name__)

# User registration route
@api_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Missing required fields"}), 400

    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({"msg": "Email already registered"}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

# User login route
@api_routes.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Missing required fields"}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({
        "msg": "Login successful",
        "access_token": access_token,
        "user": user.name
    }), 200

# Booking route (for users to book buses)
@api_routes.route('/book', methods=['POST'])
@jwt_required()
def book_bus():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    if not data or not data.get('bus') or not data.get('date') or not data.get('time'):
        return jsonify({"msg": "Missing required fields"}), 400

    booking = Booking(
        bus=data['bus'],
        date=data['date'],
        time=data['time'],
        user_id=current_user_id
    )
    db.session.add(booking)
    db.session.commit()

    return jsonify({"msg": "Booking successful"}), 201

# Get bookings for logged-in user
@api_routes.route('/bookings', methods=['GET'])
@jwt_required()
def get_bookings():
    current_user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=current_user_id).all()
    
    if not bookings:
        return jsonify({"msg": "No bookings found"}), 404

    bookings_list = [{
        "id": booking.id,
        "bus": booking.bus,
        "date": booking.date,
        "time": booking.time
    } for booking in bookings]
    return jsonify({"bookings": bookings_list}), 200
