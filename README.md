# Diabetes Prediction Web Application

A simple and user-friendly web application built with Django and Machine Learning to predict the risk of diabetes based on user health inputs.

## Features

- Clean and professional medical-style interface.
- Predicts diabetes risk using a trained ML model (Random Forest).
- Input form includes: gender, age, hypertension, heart disease, smoking history, BMI, HbA1c, blood glucose level.
- Designed for non-technical users and medical staff.

## How It Works

1. A machine learning model is trained using a publicly available dataset.
2. The model is saved as a `.pkl` file using `pickle`.
3. Users input their health information through a web form.
4. The app processes the input and displays the diabetes prediction result (Positive/Negative).

## Local Deployment Instructions

1. Clone the repository:

   git clone https://github.com/yourusername/diabetes-prediction-django.git  
   cd diabetes-prediction-django

2. Create and activate a virtual environment:

   python3 -m venv venv       (for macOS/Linux)  
   source venv/bin/activate  
   python -m venv venv        (for Windows)
   venv\Scripts\activate      

3. Install dependencies:

   pip install -r requirements.txt

4. Train the model:

   python train_model.py

5. Run database migrations:

   python manage.py makemigrations  
   python manage.py migrate

6. Start the Django development server:

   python manage.py runserver

7. Open your browser and go to:

   http://127.0.0.1:8000/

You will see the prediction form. Fill in your health data and click "Predict" to get the result.

## Built With

- Django (Python Web Framework)
- scikit-learn
- pandas & numpy
- HTML/CSS
- Random Forest Classifier


## Disclaimer

This project is for educational and demonstration purposes only. The model is not meant for real medical diagnosis or treatment.
