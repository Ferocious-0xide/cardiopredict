from app import db
from datetime import datetime

class PatientData(db.Model):
    __tablename__ = 'patient_data'
    
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    ap_hi = db.Column(db.Integer, nullable=False)
    ap_lo = db.Column(db.Integer, nullable=False)
    cholesterol = db.Column(db.Integer, nullable=False)
    gluc = db.Column(db.Integer, nullable=False)
    smoke = db.Column(db.Integer, nullable=False)
    alco = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)
    cardio = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def init_db():
    db.create_all()