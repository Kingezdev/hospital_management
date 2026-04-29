from django import forms
from .models import Patient, Illness, Treatment, PatientRecord, Appointment
from django.contrib.auth import get_user_model

User = get_user_model()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'email', 
                 'address', 'emergency_contact', 'emergency_phone', 'blood_type', 'allergies']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'allergies': forms.Textarea(attrs={'rows': 3}),
        }


class IllnessForm(forms.ModelForm):
    class Meta:
        model = Illness
        fields = ['name', 'description', 'severity', 'symptoms']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'symptoms': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter symptoms separated by commas'}),
        }


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['name', 'description', 'duration', 'cost', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = ['patient', 'illness', 'treatment', 'diagnosis_date', 'notes', 'is_active']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all().order_by('last_name', 'first_name')
        self.fields['illness'].queryset = Illness.objects.all().order_by('name')
        self.fields['treatment'].queryset = Treatment.objects.all().order_by('name')
        self.fields['treatment'].required = False


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'appointment_date', 'reason', 'status', 'notes']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'reason': forms.TextInput(attrs={'placeholder': 'Reason for appointment'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all().order_by('last_name', 'first_name')
