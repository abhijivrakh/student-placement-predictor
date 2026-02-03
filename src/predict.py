import os
import pandas as pd
import joblib
from src.preprocess import preprocess_data

# Absolute path inside Docker container
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

def predict(input_data: dict):
    # Load model
    model = joblib.load(MODEL_PATH)

    # Convert input to DataFrame
    df = pd.DataFrame([input_data])

    # Preprocess
    X_scaled, _ = preprocess_data(df, training=False)

    # Predict
    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]

    return prediction, probability
