# app/__init__.py
from flask import Flask
from .config import Config
from .extensions import db
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow() 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from .routes.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    from app.routes.route_routes import bp as route_bp
    app.register_blueprint(route_bp)

    

    return app
