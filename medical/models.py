from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    emergency_contact = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=5, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']


class Illness(models.Model):
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    symptoms = models.TextField(help_text="List of symptoms separated by commas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Treatment(models.Model):
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50, help_text="e.g., '2 weeks', '1 month'")
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_records')
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE, related_name='patient_records')
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name='patient_records', blank=True, null=True)
    diagnosis_date = models.DateField()
    notes = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.illness} ({self.diagnosis_date})"

    class Meta:
        ordering = ['-diagnosis_date']


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    )
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} with Dr. {self.doctor.last_name} on {self.appointment_date}"

    class Meta:
        ordering = ['-appointment_date']
