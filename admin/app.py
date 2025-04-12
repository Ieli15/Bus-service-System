# app.py
from flask import Flask
from extensions import db
from flask_jwt_extended import JWTManager
from routes import api_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bus_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(api_routes)

if __name__ == '__main__':
    app.run(debug=True)
