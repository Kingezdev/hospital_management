from django.urls import path
from . import views

urlpatterns = [
    # Doctor URLs
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    
    path('doctor/patients/', views.PatientListView.as_view(), name='patient_list'),
    path('doctor/patients/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('doctor/patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
    
    path('doctor/illnesses/', views.IllnessListView.as_view(), name='illness_list'),
    path('doctor/illnesses/create/', views.IllnessCreateView.as_view(), name='illness_create'),
    path('doctor/illnesses/<int:pk>/update/', views.IllnessUpdateView.as_view(), name='illness_update'),
    
    path('doctor/treatments/', views.TreatmentListView.as_view(), name='treatment_list'),
    path('doctor/treatments/create/', views.TreatmentCreateView.as_view(), name='treatment_create'),
    path('doctor/treatments/<int:pk>/update/', views.TreatmentUpdateView.as_view(), name='treatment_update'),
    
    path('doctor/records/', views.PatientRecordListView.as_view(), name='patientrecord_list'),
    path('doctor/records/create/', views.PatientRecordCreateView.as_view(), name='patientrecord_create'),
    path('doctor/records/<int:pk>/update/', views.PatientRecordUpdateView.as_view(), name='patientrecord_update'),
    
    path('doctor/appointments/', views.AppointmentListView.as_view(), name='appointment_list'),
    path('doctor/appointments/create/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('doctor/appointments/<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    
    # Admin URLs
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('admin/patients/', views.AdminPatientListView.as_view(), name='admin_patient_list'),
    path('admin/illnesses/', views.AdminIllnessListView.as_view(), name='admin_illness_list'),
    path('admin/treatments/', views.AdminTreatmentListView.as_view(), name='admin_treatment_list'),
    path('admin/records/', views.AdminPatientRecordListView.as_view(), name='admin_patientrecord_list'),
    path('admin/appointments/', views.AdminAppointmentListView.as_view(), name='admin_appointment_list'),
]
