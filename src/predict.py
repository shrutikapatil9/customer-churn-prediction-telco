import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")

sample = pd.DataFrame({
    "gender": ["Female"],
    "tenure": [5],
    "MonthlyCharges": [75.5]
})

prediction = model.predict(sample)

print(prediction)