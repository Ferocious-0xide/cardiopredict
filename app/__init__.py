# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    # Register blueprints
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app