import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load the dataset from CSV file
df = pd.read_csv("diabetes_prediction_dataset.csv")

# Convert gender column to numeric values (Male=0, Female=1, Other=2)
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1, 'Other': 2})

# Convert 'smoking_history' categorical text to numerical codes
df['smoking_history'] = df['smoking_history'].astype('category').cat.codes

# Handle missing values in the 'diabetes' column by replacing them with the most frequent value
df['diabetes'] = df['diabetes'].fillna(df['diabetes'].mode()[0])

# Drop all rows that contain any remaining missing values
df = df.dropna()

# Define the feature columns (input variables)
X = df[['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']]

# Define the target column (output variable)
y = df['diabetes']

# Create a Random Forest Classifier model
model = RandomForestClassifier()

# Train the model using the input features and target
model.fit(X, y)

# Create directory to save the trained model if it doesn't exist
os.makedirs('predictor/ml_model', exist_ok=True)

# Save the trained model as a pickle (.pkl) file inside predictor/ml_model
with open('predictor/ml_model/diabetes_model.pkl', 'wb') as f:
    pickle.dump(model, f)