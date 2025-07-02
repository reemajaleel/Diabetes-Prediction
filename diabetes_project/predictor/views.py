from django.shortcuts import render
from .forms import DiabetesForm
import numpy as np
import pickle
import os

# Load the trained machine learning model from the .pkl file
model_path = os.path.join(os.path.dirname(__file__), 'ml_model/diabetes_model.pkl')  # Get the model path relative to this file
with open(model_path, 'rb') as f:
    model = pickle.load(f)  # Load the model into memory

# Define the main view function to handle form submission and prediction
def predict_diabetes(request):
    result = None  # Initialize prediction result as None

    # Check if the form has been submitted
    if request.method == 'POST':
        form = DiabetesForm(request.POST) 
        if form.is_valid():  # Validate form data
            data = form.cleaned_data  # Extract cleaned data from the form

            # Prepare the input array for prediction
            input_data = np.array([[
                int(data['gender']),
                float(data['age']),
                int(data['hypertension']),
                int(data['heart_disease']),
                int(data['smoking_history']),
                float(data['bmi']),
                float(data['HbA1c_level']),
                float(data['blood_glucose_level']),
            ]])

            # Perform the prediction using the trained model
            prediction = model.predict(input_data)[0]  # Get the predicted class (0 or 1)

            # Convert the numeric prediction into a human-readable result
            result = 'Positive' if prediction == 1 else 'Negative'

    else:
        form = DiabetesForm()  # If not POST, just render an empty form

    # Render the template and pass the form and prediction result to the page
    return render(request, 'predictor/home.html', {'form': form, 'result': result})