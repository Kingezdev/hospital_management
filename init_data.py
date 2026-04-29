import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from medical.models import Patient, Illness, Treatment, PatientRecord, Appointment
from datetime import datetime, date, timedelta

User = get_user_model()

def create_sample_data():
    print("Creating sample data...")
    
    # Create admin user (if not exists)
    admin_user = User.objects.filter(username='admin').first()
    if not admin_user:
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@hospital.com',
            password='admin123',
            user_type='admin',
            first_name='Admin',
            last_name='User'
        )
        print("Created admin user")
    
    # Create doctor user
    doctor_user = User.objects.filter(username='doctor').first()
    if not doctor_user:
        doctor_user = User.objects.create_user(
            username='doctor',
            email='doctor@hospital.com',
            password='doctor123',
            user_type='doctor',
            first_name='John',
            last_name='Smith',
            phone='123-456-7890'
        )
        print("Created doctor user")
    
    # Create sample illnesses
    illnesses_data = [
        {
            'name': 'Common Cold',
            'description': 'A viral infectious disease of the upper respiratory tract.',
            'severity': 'low',
            'symptoms': 'Runny nose, sore throat, cough, congestion'
        },
        {
            'name': 'Influenza',
            'description': 'A viral infection that attacks your respiratory system.',
            'severity': 'medium',
            'symptoms': 'Fever, muscle aches, cough, fatigue, headache'
        },
        {
            'name': 'Hypertension',
            'description': 'High blood pressure, a long-term medical condition.',
            'severity': 'high',
            'symptoms': 'Headaches, shortness of breath, nosebleeds'
        }
    ]
    
    for illness_data in illnesses_data:
        illness, created = Illness.objects.get_or_create(
            name=illness_data['name'],
            defaults=illness_data
        )
        if created:
            print(f"Created illness: {illness.name}")
    
    # Create sample treatments
    treatments_data = [
        {
            'name': 'Rest and Fluids',
            'description': 'Conservative treatment for viral infections',
            'duration': '7-10 days',
            'cost': '50.00',
            'status': 'planned'
        },
        {
            'name': 'Antibiotics',
            'description': 'Medication to treat bacterial infections',
            'duration': '5-7 days',
            'cost': '150.00',
            'status': 'planned'
        },
        {
            'name': 'Blood Pressure Medication',
            'description': 'Medication to control hypertension',
            'duration': 'Ongoing',
            'cost': '100.00',
            'status': 'planned'
        }
    ]
    
    for treatment_data in treatments_data:
        treatment, created = Treatment.objects.get_or_create(
            name=treatment_data['name'],
            defaults=treatment_data
        )
        if created:
            print(f"Created treatment: {treatment.name}")
    
    # Create sample patients
    patients_data = [
        {
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'date_of_birth': date(1985, 5, 15),
            'gender': 'F',
            'phone': '555-0101',
            'email': 'alice.j@email.com',
            'address': '123 Main St, City, State 12345',
            'emergency_contact': 'Bob Johnson',
            'emergency_phone': '555-0102',
            'blood_type': 'O+',
            'allergies': 'Penicillin'
        },
        {
            'first_name': 'Robert',
            'last_name': 'Williams',
            'date_of_birth': date(1978, 8, 22),
            'gender': 'M',
            'phone': '555-0201',
            'email': 'robert.w@email.com',
            'address': '456 Oak Ave, Town, State 67890',
            'emergency_contact': 'Mary Williams',
            'emergency_phone': '555-0202',
            'blood_type': 'A+',
            'allergies': 'None'
        },
        {
            'first_name': 'Emily',
            'last_name': 'Davis',
            'date_of_birth': date(1992, 3, 10),
            'gender': 'F',
            'phone': '555-0301',
            'email': 'emily.d@email.com',
            'address': '789 Pine Rd, Village, State 13579',
            'emergency_contact': 'David Davis',
            'emergency_phone': '555-0302',
            'blood_type': 'B+',
            'allergies': 'Pollen'
        }
    ]
    
    for patient_data in patients_data:
        patient, created = Patient.objects.get_or_create(
            phone=patient_data['phone'],
            defaults=patient_data
        )
        if created:
            print(f"Created patient: {patient.first_name} {patient.last_name}")
    
    # Create sample patient records
    common_cold = Illness.objects.get(name='Common Cold')
    influenza = Illness.objects.get(name='Influenza')
    hypertension = Illness.objects.get(name='Hypertension')
    
    rest_fluids = Treatment.objects.get(name='Rest and Fluids')
    antibiotics = Treatment.objects.get(name='Antibiotics')
    bp_medication = Treatment.objects.get(name='Blood Pressure Medication')
    
    patients = Patient.objects.all()
    
    if len(patients) >= 3:
        # Patient 1 - Common Cold
        record1, created = PatientRecord.objects.get_or_create(
            patient=patients[0],
            doctor=doctor_user,
            illness=common_cold,
            defaults={
                'treatment': rest_fluids,
                'diagnosis_date': date.today() - timedelta(days=5),
                'notes': 'Patient presents with symptoms of common cold. Prescribed rest and plenty of fluids.',
                'is_active': True
            }
        )
        if created:
            print(f"Created patient record for {patients[0]}")
        
        # Patient 2 - Influenza
        record2, created = PatientRecord.objects.get_or_create(
            patient=patients[1],
            doctor=doctor_user,
            illness=influenza,
            defaults={
                'treatment': antibiotics,
                'diagnosis_date': date.today() - timedelta(days=3),
                'notes': 'Patient diagnosed with influenza. Started antibiotic treatment.',
                'is_active': True
            }
        )
        if created:
            print(f"Created patient record for {patients[1]}")
        
        # Patient 3 - Hypertension
        record3, created = PatientRecord.objects.get_or_create(
            patient=patients[2],
            doctor=doctor_user,
            illness=hypertension,
            defaults={
                'treatment': bp_medication,
                'diagnosis_date': date.today() - timedelta(days=10),
                'notes': 'Patient with hypertension. Started blood pressure medication.',
                'is_active': True
            }
        )
        if created:
            print(f"Created patient record for {patients[2]}")
    
    # Create sample appointments
    appointment_data = [
        {
            'patient': patients[0],
            'doctor': doctor_user,
            'appointment_date': datetime.now() + timedelta(days=1),
            'reason': 'Follow-up visit',
            'status': 'scheduled',
            'notes': 'Follow-up for cold symptoms'
        },
        {
            'patient': patients[1],
            'doctor': doctor_user,
            'appointment_date': datetime.now() + timedelta(days=3),
            'reason': 'Check-up',
            'status': 'scheduled',
            'notes': 'Regular check-up'
        },
        {
            'patient': patients[2],
            'doctor': doctor_user,
            'appointment_date': datetime.now() - timedelta(days=1),
            'reason': 'Emergency visit',
            'status': 'completed',
            'notes': 'Emergency visit completed'
        }
    ]
    
    for appt_data in appointment_data:
        appointment, created = Appointment.objects.get_or_create(
            patient=appt_data['patient'],
            doctor=appt_data['doctor'],
            appointment_date=appt_data['appointment_date'],
            defaults=appt_data
        )
        if created:
            print(f"Created appointment for {appointment.patient}")
    
    print("Sample data creation complete!")

if __name__ == '__main__':
    create_sample_data()
