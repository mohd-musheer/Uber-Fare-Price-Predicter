from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://uber-fare-price-predicter.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load(BASE_DIR / "UberFarePredictor.pkl")


class DataModel(BaseModel):
    passenger_count: int
    hour: int
    weekday: int
    month: int
    year: int
    is_weekday: int
    is_night: int
    distance_km: float


@app.post("/predict")
def predict(data: DataModel):
    df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(df)[0]
    return {"predicted_fare": round(float(prediction), 2)}


@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE_DIR / "index.html").read_text(encoding="utf-8")
