import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://3.109.49.203:8000/predict"

st.title("Customer Churn Prediction System")

st.write("Enter customer details to predict churn probability.")

# Input fields
total_orders = st.number_input("Total Orders", min_value=0.0)
total_sales = st.number_input("Total Sales", min_value=0.0)
total_quantity = st.number_input("Total Quantity", min_value=0.0)
recency = st.number_input("Recency (days since last purchase)", min_value=0.0)
lifespan = st.number_input("Customer Lifespan", min_value=0.0)
avg_order_value = st.number_input("Average Order Value", min_value=0.0)
avg_monthly_spend = st.number_input("Average Monthly Spend", min_value=0.0)
age = st.number_input("Customer Age", min_value=0.0)

# Predict button
if st.button("Predict Churn"):
    
    data = {
        "total_orders": total_orders,
        "total_sales": total_sales,
        "total_quantity": total_quantity,
        "recency": recency,
        "lifespan": lifespan,
        "avg_order_value": avg_order_value,
        "avg_monthly_spend": avg_monthly_spend,
        "age": age
    }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        result = response.json()
        
        st.success(f"Churn Probability: {result['churn_probability']:.2f}")
        
        if result['churn_prediction'] == 1:
            st.error("Customer is likely to churn")
        else:
            st.success("Customer is not likely to churn")
    
    else:
        st.error("Error connecting to prediction API")
