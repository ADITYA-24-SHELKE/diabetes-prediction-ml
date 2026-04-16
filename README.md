# Diabetes Risk Predictor

A web app that uses your trained SVC model to predict diabetes risk.

## Files
- `diabetes_predictor.html` — The web UI (works standalone OR with the Flask backend)
- `app.py` — Flask backend that calls your actual `.pkl` model
- `diabetes_model.pkl` — Your trained SVC model
- `scaler.pkl` — Your StandardScaler

## Option 1: Open HTML directly (no Python needed)
Just open `diabetes_predictor.html` in any browser.
It uses a built-in JS heuristic based on clinical thresholds.

## Option 2: Run with your real SVC model (recommended)

### Install dependencies
```bash
pip install flask scikit-learn joblib numpy
```

### Place your pkl files in the same folder, then run:
```bash
python app.py
```

### Open in browser:
```
http://localhost:5000
```

The HTML will automatically detect the Flask backend and use your **actual SVC model** for predictions.

## Input Features
| Feature | Description | Typical Range |
|---|---|---|
| Pregnancies | Number of pregnancies | 0–17 |
| Glucose | Plasma glucose (mg/dL) | 0–300 |
| Blood Pressure | Diastolic BP (mm Hg) | 0–140 |
| Skin Thickness | Triceps skinfold (mm) | 0–100 |
| Insulin | 2-hr serum insulin (mu U/ml) | 0–900 |
| BMI | Body Mass Index (kg/m²) | 0–70 |
| Diabetes Pedigree | Genetic risk score | 0.000–2.500 |
| Age | Age in years | 1–100 |

## Output
- **0** = Lower risk (no diabetes predicted)
- **1** = Higher risk (diabetes predicted)
