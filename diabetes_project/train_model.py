import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

df = pd.read_csv("diabetes_prediction_dataset.csv")

df['gender'] = df['gender'].map({'Male': 0, 'Female': 1, 'Other': 2})
df['smoking_history'] = df['smoking_history'].astype('category').cat.codes  
df['diabetes'] = df['diabetes'].fillna(df['diabetes'].mode()[0])         

df = df.dropna()

X = df[['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history','bmi', 'HbA1c_level', 'blood_glucose_level']]
y = df['diabetes']

model = RandomForestClassifier()
model.fit(X, y)

os.makedirs('predictor/ml_model', exist_ok=True)
with open('predictor/ml_model/diabetes_model.pkl', 'wb') as f:
    pickle.dump(model, f)
