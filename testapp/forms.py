from django import forms
from testapp.models import Doctor,Patient

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"

        widgets={
        'doctor_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Doctor Name:'}),
        'mobile_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile Number:'}),
        'hospital_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Hospital Name:'}),
        'specialization':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Specialization area:'}),
        'experience':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Experience:'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"


        widgets={
        'patient_name':forms.TextInput(attrs={'class':'form-control'}),
        'mobile_number':forms.TextInput(attrs={'class':'form-control'}),
        'age':forms.TextInput(attrs={'class':'form-control'}),
        'gender':forms.Select(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),




        }
