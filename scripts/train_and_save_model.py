# scripts/train_and_save_model.py
import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from app import create_app
from app.models.predictor import CardiovascularPredictor
import pandas as pd

def train_initial_model():
    print("Loading data...")
    # Load your CSV data
    data_path = os.path.join(project_root, 'cardio_train.csv')
    df = pd.read_csv(data_path, sep=';')
    
    print("Training model...")
    app = create_app()
    with app.app_context():
        predictor = CardiovascularPredictor()
        predictor.train(df)  # Pass the dataframe to train method
        
        # Create models directory if it doesn't exist
        os.makedirs(os.path.join(project_root, 'models'), exist_ok=True)
        
        # Save the model
        predictor.save(os.path.join(project_root, 'models/cardio_model.joblib'))
        print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_initial_model()


from app.utils.model_storage import ModelStorage

def train_initial_model():
    print("Loading data...")
    df = pd.read_csv(data_path, sep=';')
    
    print("Training model...")
    app = create_app()
    with app.app_context():
        predictor = CardiovascularPredictor()
        predictor.train(df)
        predictor.save()  # This will now save to database
        print("Model trained and saved to database!")    