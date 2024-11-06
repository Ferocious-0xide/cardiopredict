from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from flask_cors import CORS  

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    @app.route('/')  # Add a root route
    def home():
        return jsonify({'message': 'Welcome to CardioPredict API'})
    
    @app.route('/test')
    def test_route():
        return jsonify({'message': 'Test route working'})
    
    return app

from app.api import routes