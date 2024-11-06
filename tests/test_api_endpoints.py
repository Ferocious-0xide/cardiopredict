# tests/test_api_endpoints.py
import json
import pytest

def test_health_check(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_predict_endpoint(client):
    test_data = {
        'age': 18393,
        'gender': 2,
        'height': 168,
        'weight': 62.0,
        'ap_hi': 110,
        'ap_lo': 80,
        'cholesterol': 1,
        'gluc': 1,
        'smoke': 0,
        'alco': 0,
        'active': 1
    }
    
    response = client.post(
        '/api/v1/predict',
        data=json.dumps(test_data),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    assert 'prediction' in response.json
    assert 'probability' in response.json
    assert 'confidence' in response.json
    assert 'risk_level' in response.json

def test_batch_predict_endpoint(client):
    test_data = [
        {
            'age': 18393,
            'gender': 2,
            'height': 168,
            'weight': 62.0,
            'ap_hi': 110,
            'ap_lo': 80,
            'cholesterol': 1,
            'gluc': 1,
            'smoke': 0,
            'alco': 0,
            'active': 1
        },
        {
            'age': 20228,
            'gender': 1,
            'height': 156,
            'weight': 85.0,
            'ap_hi': 140,
            'ap_lo': 90,
            'cholesterol': 3,
            'gluc': 1,
            'smoke': 0,
            'alco': 0,
            'active': 1
        }
    ]
    
    response = client.post(
        '/api/v1/predict/batch',
        data=json.dumps(test_data),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 2
