# 🚕 Uber Fare Price Predictor (Machine Learning Project)

Predict the taxi fare price based on ride details such as distance, passengers and time — similar to how Uber/Ola fare estimation works.
Live Model test  : https://uber-fare-price-predicter.onrender.com

API : https://uber-fare-price-predicter.onrender.com/predict
This project uses:
- **Python**
- **Scikit-Learn**
- **RandomForestRegressor / (Optional) Ensemble with XGBoost**
- **Feature Engineering**
- **Joblib for Model Saving**
- **Distance Calculation with Haversine Formula**
- **FastAPI Support Ready**
- **Frontend (Optional)**

---

## 📌 Features
✔ Predict fare price based on:
- Passenger Count
- Time of Day
- Day of Week
- Month & Year
- Weekend/Night Indicator
- Trip Distance (in km)

✔ Feature Engineering Includes:
- Haversine distance (lat/long → km)
- Weekend/Night flags
- Date-time extraction

✔ Model Deployment Ready:
- `fare_model.pkl`
- FastAPI Endpoint Support
- Can be Dockerized

---

## 🧠 Tech Used
| Category | Technology |
|----------|-------------|
| Language | Python |
| ML Models | RandomForest / XGBoost |
| Deployment | FastAPI (Optional) |
| Model Saving | Joblib |
| Data Handling | Pandas, NumPy |
| Feature Scaling | ColumnTransformer |

---

## 📂 Project Structure

