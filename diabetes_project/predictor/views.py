from django.shortcuts import render
from .forms import DiabetesForm
import numpy as np
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), 'ml_model/diabetes_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def predict_diabetes(request):
    result = None
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
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
            prediction = model.predict(input_data)[0]
            result = 'Positive' if prediction == 1 else 'Negative'
    else:
        form = DiabetesForm()
    return render(request, 'predictor/home.html', {'form': form, 'result': result})
