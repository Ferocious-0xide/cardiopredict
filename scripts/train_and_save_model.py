# scripts/train_and_save_model.py
import os
import sys
from pathlib import Path
import pandas as pd
import logging

# Add project root to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from app import create_app
from app.models.predictor import CardiovascularPredictor

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def find_data_file():
    """Find the cardio_train.csv file in common locations"""
    possible_locations = [
        os.path.join(project_root, 'cardio_train.csv'),
        os.path.expanduser('~/Downloads/cardio_train.csv'),
        os.path.expanduser('~/Desktop/cardio_train.csv')
    ]
    
    for location in possible_locations:
        if os.path.exists(location):
            logger.info(f"Found data file at: {location}")
            return location
    
    raise FileNotFoundError(
        "Could not find cardio_train.csv. Please ensure it's in one of these locations:\n" +
        "\n".join(possible_locations)
    )

def train_initial_model():
    try:
        print("Loading data...")
        data_path = find_data_file()
        df = pd.read_csv(data_path, sep=';')
        
        logger.info(f"Loaded {len(df)} records")
        logger.info("Data sample:")
        logger.info(df.head())
        
        print("Training model...")
        app = create_app()
        with app.app_context():
            predictor = CardiovascularPredictor()
            metrics = predictor.train(df)
            
            logger.info("Training metrics:")
            logger.info(f"Train score: {metrics['train_score']:.3f}")
            logger.info(f"Test score: {metrics['test_score']:.3f}")
            
            # Optional: Save to file system as backup
            models_dir = os.path.join(project_root, 'models')
            os.makedirs(models_dir, exist_ok=True)
            predictor.save()
            
            print("Model trained and saved successfully!")
            return metrics
            
    except FileNotFoundError as e:
        logger.error(f"Data file error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Training error: {str(e)}")
        raise

def main():
    try:
        train_initial_model()
    except Exception as e:
        logger.error(f"Failed to train model: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()