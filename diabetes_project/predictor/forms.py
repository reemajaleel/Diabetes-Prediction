from django import forms

class DiabetesForm(forms.Form):
    gender = forms.ChoiceField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')])
    age = forms.FloatField()
    hypertension = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    heart_disease = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    smoking_history = forms.ChoiceField(choices=[(0, 'never'), (1, 'No Info'), (2, 'former'),(3, 'current'), (4, 'not current')])
    bmi = forms.FloatField()
    HbA1c_level = forms.FloatField()
    blood_glucose_level = forms.FloatField()
