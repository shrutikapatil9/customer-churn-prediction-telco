# 📊 Telco Customer Churn Prediction

## Overview

This project predicts whether a telecom customer is likely to churn based on customer information. A machine learning model was trained using historical customer data and deployed as an interactive Streamlit web application.

## Live Demo

Streamlit App:
https://customer-churn-prediction-telco-vdrfexkzerhgypruzue37d.streamlit.app/

## Features

* Predict customer churn in real time
* User-friendly Streamlit interface
* Machine learning model built with Scikit-learn
* Data preprocessing and feature scaling pipeline
* Deployed online using Streamlit Community Cloud

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Git & GitHub

## Project Workflow

1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Streamlit App Development
7. Cloud Deployment

## Input Features

* Tenure
* Monthly Charges

## Model

The project uses a machine learning classification model to predict whether a customer is likely to churn.

## Installation

Clone the repository:

```bash
git clone https://github.com/shrutikapatil9/customer-churn-prediction-telco.git
cd customer-churn-prediction-telco
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Repository Structure

```text
customer-churn-prediction-telco/
│
├── app.py
├── requirements.txt
├── README.md
├── models/
│   └── churn_model.pkl
└── notebooks/
```

## Future Improvements

* Use additional customer features for higher prediction accuracy
* Compare multiple machine learning algorithms
* Add model explainability using SHAP
* Improve UI/UX design

## Author

Shrutika Patil



GitHub: https://github.com/shrutikapatil9

