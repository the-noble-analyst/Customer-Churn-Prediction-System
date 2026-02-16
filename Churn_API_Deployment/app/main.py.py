from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI()

# Load trained model
model = joblib.load("best_churn_model.pkl")

# Define request body structure
class CustomerData(BaseModel):
    total_orders: float
    total_sales: float
    total_quantity: float
    recency: float
    lifespan: float
    avg_order_value: float
    avg_monthly_spend: float
    age: float

# Home route
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

# Prediction route
@app.post("/predict")
def predict(data: CustomerData):

    # Create feature array in correct order
    features = np.array([[
        data.total_orders,
        data.total_sales,
        data.total_quantity,
        data.recency,
        data.lifespan,
        data.avg_order_value,
        data.avg_monthly_spend,
        data.age
    ]])

    # Predict probability
    prob = model.predict_proba(features)[0][1]

    # Apply threshold
    threshold = 0.30
    prediction = 1 if prob >= threshold else 0

    return {
        "churn_probability": float(prob),
        "churn_prediction": prediction
    }