from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

app = FastAPI()
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.post("/predict")
def predict(features: list):
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)
    return {"prediction": float(prediction[0])}