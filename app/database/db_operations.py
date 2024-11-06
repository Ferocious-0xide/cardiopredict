# app/database/db_operations.py
from app import db
from datetime import datetime
from sqlalchemy import LargeBinary

class ModelStorage(db.Model):
    __tablename__ = 'model_storage'
    
    id = db.Column(db.Integer, primary_key=True, default=1)
    model_binary = db.Column(LargeBinary)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

def init_db():
    db.create_all()