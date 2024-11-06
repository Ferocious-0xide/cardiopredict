# app/models/predictor.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CardiovascularPredictor:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.feature_columns = [
            'age', 'gender', 'height', 'weight', 
            'ap_hi', 'ap_lo', 'cholesterol', 'gluc',
            'smoke', 'alco', 'active'
        ]
        # Try to load model from database
        try:
            self.model, self.scaler = ModelStorage.load_model_from_db()
            if self.model:
                logger.info("Model loaded from database")
        except Exception as e:
            logger.warning(f"Could not load model: {e}")
    
    def train(self, df):
        """Train the model using the provided dataframe"""
        logger.info("Loading training data...")
        
        # Prepare features
        X = df[self.feature_columns]
        y = df['cardio']
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        logger.info("Training model...")
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate
        train_score = self.model.score(X_train_scaled, y_train)
        test_score = self.model.score(X_test_scaled, y_test)
        
        logger.info(f"Training accuracy: {train_score:.3f}")
        logger.info(f"Test accuracy: {test_score:.3f}")
        
        return {
            'train_score': train_score,
            'test_score': test_score
        }
    
    def predict(self, features):
        """Make predictions for new data"""
        try:
            if self.model is None or not hasattr(self.scaler, 'mean_'):
                self.load('models/cardio_model.joblib')
                logger.info("Loaded model for prediction")

            # Prepare features
            df = pd.DataFrame([features])
            X = df[self.feature_columns]
            
            # Scale features
            X_scaled = self.scaler.transform(X)
            
            # Get prediction and probability
            prediction = self.model.predict(X_scaled)[0]
            probability = self.model.predict_proba(X_scaled)[0]
            
            return {
                'prediction': int(prediction),
                'probability': float(probability[1]),
                'confidence': float(max(probability))
            }
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise
    
    def save(self):
        """Save model to database"""
        ModelStorage.save_model_to_db(self.model, self.scaler)
    
    def load(self, filepath='models/cardio_model.joblib'):
        """Load model and scaler"""
        artifacts = joblib.load(filepath)
        self.model = artifacts['model']
        self.scaler = artifacts['scaler']
        logger.info(f"Model loaded from {filepath}")
        return self