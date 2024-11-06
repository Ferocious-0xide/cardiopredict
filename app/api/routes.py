from flask import jsonify, request
from app.api import bp
from app.models.predictor import PatientData, db

@bp.before_app_request  # Changed from before_app_first_request
def init_app():
    """Initialize app before first request"""
    pass

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})