# app/routes.py
from flask import Blueprint, render_template, request
from app.models.predictor import CardiovascularPredictor
import logging

logger = logging.getLogger(__name__)

# Create the blueprint
bp = Blueprint('main', __name__)

# Define tooltips
TOOLTIPS = {
    'age': 'Enter age in years',
    'gender': 'Select biological gender',
    'height': 'Height in centimeters',
    'weight': 'Weight in kilograms',
    'ap_hi': 'Systolic blood pressure (upper number)',
    'ap_lo': 'Diastolic blood pressure (lower number)',
    'cholesterol': 'Cholesterol level from recent blood test',
    'gluc': 'Glucose level from recent blood test',
    'smoke': 'Regular smoking habit',
    'alco': 'Regular alcohol consumption',
    'active': 'Regular physical activity'
}

@bp.route('/')
def home():
    return render_template('predict.html', tooltips=TOOLTIPS)

@bp.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Convert age from years to days
            age_in_days = int(float(request.form['age']) * 365.25)
            
            prediction_data = {
                'age': age_in_days,
                'gender': int(request.form['gender']),
                'height': float(request.form['height']),
                'weight': float(request.form['weight']),
                'ap_hi': int(request.form['ap_hi']),
                'ap_lo': int(request.form['ap_lo']),
                'cholesterol': int(request.form['cholesterol']),
                'gluc': int(request.form['gluc']),
                'smoke': int(request.form['smoke']),
                'alco': int(request.form['alco']),
                'active': int(request.form['active'])
            }
            
            predictor = CardiovascularPredictor()
            result = predictor.predict(prediction_data)
            
            prediction = {
                'result': 'Positive' if result['prediction'] == 1 else 'Negative',
                'confidence': f"{result['confidence']*100:.1f}",
                'risk_level': 'High' if result.get('probability', 0) > 0.7 else 'Medium' if result.get('probability', 0) > 0.3 else 'Low'
            }
            
            return render_template('predict.html', prediction=prediction, tooltips=TOOLTIPS)
            
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            error_message = "An error occurred during prediction. Please ensure the model is trained and try again."
            return render_template('predict.html', error=error_message, tooltips=TOOLTIPS)
    
    return render_template('predict.html', tooltips=TOOLTIPS)