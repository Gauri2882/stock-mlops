from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class Features(BaseModel):
    features: list[float]

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.post("/predict")
def predict(input: Features):
    scaled = scaler.transform([input.features])
    prediction = model.predict(scaled)[0]
    return {"prediction": float(prediction)}