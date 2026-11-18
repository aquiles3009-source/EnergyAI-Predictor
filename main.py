from fastapi.responses import FileResponse
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Energy Consumption AI")

# Locate the model relative to this Python file
MODEL_PATH = Path(__file__).resolve().parent / "energy_model.joblib"

# Load the trained model
model = joblib.load(MODEL_PATH)


# Define the input data structure
class HouseData(BaseModel):
    num_occupants: int = Field(ge=1, le=6)
    avg_temperature: float = Field(ge=0, le=30)
    house_size: float = Field(ge=40, le=250)


# Home endpoint
@app.get("/")
def home():
    html_path = Path(__file__).resolve().parent / "index.html"
    return FileResponse(html_path)
    
    #return {"message": "Energy Consumption AI is running"}# used for testing in Fastapi web browser http://http://127.0.0.1:8000/docs


# Prediction endpoint
@app.post("/predict")
def predict(data: HouseData):

    features = pd.DataFrame([{
        "num_occupants": data.num_occupants,
        "avg_temperature": data.avg_temperature,
        "house_size": data.house_size
    }])

    prediction = model.predict(features)[0]

    return {
        "predicted_energy_kwh": round(float(prediction), 2)
    }