from django.contrib import admin
from .models import Patient, Illness, Treatment, PatientRecord, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'blood_type', 'created_at')
    list_filter = ('gender', 'blood_type', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    ordering = ('last_name', 'first_name')


@admin.register(Illness)
class IllnessAdmin(admin.ModelAdmin):
    list_display = ('name', 'severity', 'created_at')
    list_filter = ('severity', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'cost', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(PatientRecord)
class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'illness', 'treatment', 'diagnosis_date', 'is_active')
    list_filter = ('illness', 'doctor', 'is_active', 'diagnosis_date')
    search_fields = ('patient__first_name', 'patient__last_name', 'illness__name', 'notes')
    ordering = ('-diagnosis_date',)
    date_hierarchy = 'diagnosis_date'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'reason', 'status')
    list_filter = ('status', 'appointment_date', 'doctor')
    search_fields = ('patient__first_name', 'patient__last_name', 'reason', 'notes')
    ordering = ('-appointment_date',)
    date_hierarchy = 'appointment_date'
