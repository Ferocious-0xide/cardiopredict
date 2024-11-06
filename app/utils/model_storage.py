# app/utils/model_storage.py
import joblib
import io
import logging
from app import db
from sqlalchemy import text

logger = logging.getLogger(__name__)

class ModelStorage:
    @staticmethod
    def save_model_to_db(model, scaler):
        try:
            bio = io.BytesIO()
            joblib.dump({'model': model, 'scaler': scaler}, bio)
            binary_model = bio.getvalue()
            
            # Store in database using proper text declaration
            sql = text("""
                INSERT INTO model_storage (id, model_binary) 
                VALUES (1, :model_binary)
                ON CONFLICT (id) 
                DO UPDATE SET model_binary = EXCLUDED.model_binary
            """)
            db.session.execute(sql, {'model_binary': binary_model})
            db.session.commit()
            logger.info("Model saved to database")
        except Exception as e:
            logger.error(f"Error saving model to database: {e}")
            raise

    @staticmethod
    def load_model_from_db():
        try:
            sql = text("""
                SELECT model_binary FROM model_storage WHERE id = 1 LIMIT 1
            """)
            result = db.session.execute(sql).fetchone()
            
            if result:
                bio = io.BytesIO(result[0])
                artifacts = joblib.load(bio)
                logger.info("Model loaded from database")
                return artifacts['model'], artifacts['scaler']
            return None, None
        except Exception as e:
            logger.error(f"Error loading model from database: {e}")
            return None, None