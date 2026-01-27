import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

def preprocess_data(df, training=True):
    """
    Handles preprocessing for both training and prediction
    """
    # Target handling (only during training)
    if training:
        df['Placed'] = df['Placed'].map({'Yes': 1, 'No': 0})
        X = df.drop('Placed', axis=1)
        y = df['Placed']
    else:
        X = df
        y = None

    # Encode categorical columns
    categorical_cols = X.select_dtypes(include='object').columns
    encoder = LabelEncoder()

    for col in categorical_cols:
        X[col] = encoder.fit_transform(X[col])

    # Scaling
    scaler = StandardScaler()

    if training:
        X_scaled = scaler.fit_transform(X)
        joblib.dump(scaler, "scaler.pkl")
    else:
        scaler = joblib.load("scaler.pkl")
        X_scaled = scaler.transform(X)

    return X_scaled, y