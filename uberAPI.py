from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib, pandas as pd
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://uber-fare-price-predicter.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("UberFarePredictor.pkl")

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
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return {"predicted_fare": round(float(prediction), 2)}

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html").read()