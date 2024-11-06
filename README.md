# CardioPredict

A machine learning-powered web application for cardiovascular disease prediction, built with Flask and scikit-learn. The application provides real-time predictions based on patient health metrics and lifestyle factors.

## Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL
- pyenv (recommended for Python version management)
- Heroku CLI (for deployment)

### Local Development

1. Clone and set up environment:
```bash
# Clone repository
git clone https://github.com/yourusername/cardiopredict.git
cd cardiopredict

# Create and activate virtual environment
pyenv virtualenv 3.8.12 cardiopredict-env
pyenv local cardiopredict-env

# Install dependencies
pip install -r requirements.txt
```

2. Database setup:
```bash
# Create PostgreSQL database
createdb cardiopredict

# Set environment variables
export FLASK_APP=wsgi.py
export FLASK_ENV=development
export DATABASE_URL=postgresql://localhost/cardiopredict
```

3. Initialize and run:
```bash
# Train initial model
python scripts/train_and_save_model.py

# Run application
flask run
```

Visit `http://localhost:5000` in your browser.

## Project Structure
```
cardiopredict/
├── app/                    # Application code
│   ├── __init__.py        # App initialization
│   ├── models/            # ML model implementation
│   ├── templates/         # HTML templates
│   └── routes.py          # URL routes
├── config/                # Configuration
├── models/                # Saved ML models
├── scripts/               # Utility scripts
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku configuration
└── wsgi.py               # WSGI entry point
```

## Deploying to Heroku

1. Initial setup:
```bash
# Login to Heroku
heroku login

# Create new app
heroku create cardiopredict
```

2. Configure database:
```bash
# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set FLASK_APP=wsgi.py
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(24))")
```

3. Deploy:
```bash
# Deploy application
git push heroku main

# Initialize database and train model
heroku run python scripts/train_and_save_model.py
```

## Features

### Core Functionality
- Cardiovascular disease risk prediction
- Real-time form validation
- Interactive tooltips for data input
- Confidence scores and risk levels
- Responsive design with Tailwind CSS

### Technical Features
- Logistic Regression model
- Feature scaling and validation
- PostgreSQL database integration
- RESTful API endpoints
- Error handling and logging

## API Endpoints

- `GET /`: Main prediction interface
- `POST /predict`: Make prediction
- `GET /api/v1/health`: Health check

## Model Information

The prediction model uses the following features:
- Age
- Gender
- Height and Weight
- Blood Pressure (Systolic/Diastolic)
- Cholesterol Levels
- Glucose Levels
- Smoking Status
- Alcohol Intake
- Physical Activity

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Dataset source: [Cardiovascular Disease Dataset on Kaggle](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)
- Built with Flask, scikit-learn, and Tailwind CSS