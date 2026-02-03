import pandas as pd
import joblib
import os
from src.preprocess import preprocess_data

# Absolute-safe path (works locally + Docker + Render)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(MODEL_PATH)


def predict(input_data: dict):
    df = pd.DataFrame([input_data])

    X_scaled, _ = preprocess_data(df, training=False)

    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]

    return prediction, probability
