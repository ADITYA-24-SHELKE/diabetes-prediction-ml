"""
Diabetes Prediction Flask Backend
Run: python app.py
Then open: http://localhost:5000
"""

from flask import Flask, request, jsonify, send_from_directory
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='.')

# Load model and scaler once at startup
MODEL_PATH = 'diabetes_model.pkl'
SCALER_PATH = 'scaler.pkl'

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

FEATURES = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

@app.route('/')
def index():
    return send_from_directory('.', 'diabetes_predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features in correct order
        features = [float(data[f]) for f in FEATURES]
        X = np.array(features).reshape(1, -1)
        
        # Scale and predict
        X_scaled = scaler.transform(X)
        prediction = model.predict(X_scaled)[0]
        
        # Try to get probability if supported
        prob = None
        if hasattr(model, 'predict_proba'):
            prob = float(model.predict_proba(X_scaled)[0][1])
        
        return jsonify({
            'prediction': int(prediction),
            'diabetic': bool(prediction == 1),
            'probability': prob
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("Starting Diabetes Predictor server...")
    print("Open your browser at: http://localhost:5000")
    app.run(debug=True, port=5000)
