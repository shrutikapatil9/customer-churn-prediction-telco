import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("models/churn_model.pkl")

st.title("Telco Customer Churn Prediction")

# -----------------------
# Inputs
# -----------------------
customerID = st.text_input("Customer ID", "0001")

gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.slider("Tenure", 0, 72, 12)
monthly_charges = st.number_input("MonthlyCharges", min_value=0.0)

phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

total_charges = float(tenure * monthly_charges)

# -----------------------
# Prediction
# -----------------------
if st.button("Predict"):

    input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges]
})

    prediction = model.predict(input_data)

    st.subheader("Prediction")
    st.write("Churn" if prediction[0] == 1 else "No Churn")