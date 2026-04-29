from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Patient, Illness, Treatment, PatientRecord, Appointment
from .forms import PatientForm, IllnessForm, TreatmentForm, PatientRecordForm, AppointmentForm


class IsDoctorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == 'doctor'


class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == 'admin'


class IsDoctorOrAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type in ['doctor', 'admin']


# Doctor Views
@login_required
def doctor_dashboard(request):
    if request.user.user_type != 'doctor':
        return redirect('dashboard')
    
    context = {
        'total_patients': Patient.objects.count(),
        'total_appointments': Appointment.objects.filter(doctor=request.user).count(),
        'upcoming_appointments': Appointment.objects.filter(
            doctor=request.user, 
            status='scheduled'
        ).order_by('appointment_date')[:5],
        'recent_records': PatientRecord.objects.filter(
            doctor=request.user
        ).order_by('-created_at')[:5],
    }
    return render(request, 'medical/doctor_dashboard.html', context)


class PatientListView(LoginRequiredMixin, IsDoctorMixin, ListView):
    model = Patient
    template_name = 'medical/patient_list.html'
    context_object_name = 'patients'
    paginate_by = 10

    def get_queryset(self):
        queryset = Patient.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search) | 
                Q(last_name__icontains=search) |
                Q(phone__icontains=search)
            )
        return queryset


class PatientCreateView(LoginRequiredMixin, IsDoctorMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'medical/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        messages.success(self.request, 'Patient created successfully!')
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, IsDoctorMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'medical/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        messages.success(self.request, 'Patient updated successfully!')
        return super().form_valid(form)


class IllnessListView(LoginRequiredMixin, IsDoctorMixin, ListView):
    model = Illness
    template_name = 'medical/illness_list.html'
    context_object_name = 'illnesses'
    paginate_by = 10


class IllnessCreateView(LoginRequiredMixin, IsDoctorMixin, CreateView):
    model = Illness
    form_class = IllnessForm
    template_name = 'medical/illness_form.html'
    success_url = reverse_lazy('illness_list')

    def form_valid(self, form):
        messages.success(self.request, 'Illness created successfully!')
        return super().form_valid(form)


class IllnessUpdateView(LoginRequiredMixin, IsDoctorMixin, UpdateView):
    model = Illness
    form_class = IllnessForm
    template_name = 'medical/illness_form.html'
    success_url = reverse_lazy('illness_list')

    def form_valid(self, form):
        messages.success(self.request, 'Illness updated successfully!')
        return super().form_valid(form)


class TreatmentListView(LoginRequiredMixin, IsDoctorMixin, ListView):
    model = Treatment
    template_name = 'medical/treatment_list.html'
    context_object_name = 'treatments'
    paginate_by = 10


class TreatmentCreateView(LoginRequiredMixin, IsDoctorMixin, CreateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'medical/treatment_form.html'
    success_url = reverse_lazy('treatment_list')

    def form_valid(self, form):
        messages.success(self.request, 'Treatment created successfully!')
        return super().form_valid(form)


class TreatmentUpdateView(LoginRequiredMixin, IsDoctorMixin, UpdateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'medical/treatment_form.html'
    success_url = reverse_lazy('treatment_list')

    def form_valid(self, form):
        messages.success(self.request, 'Treatment updated successfully!')
        return super().form_valid(form)


class PatientRecordListView(LoginRequiredMixin, IsDoctorMixin, ListView):
    model = PatientRecord
    template_name = 'medical/patientrecord_list.html'
    context_object_name = 'records'
    paginate_by = 10

    def get_queryset(self):
        return PatientRecord.objects.filter(doctor=self.request.user)


class PatientRecordCreateView(LoginRequiredMixin, IsDoctorMixin, CreateView):
    model = PatientRecord
    form_class = PatientRecordForm
    template_name = 'medical/patientrecord_form.html'
    success_url = reverse_lazy('patientrecord_list')

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        messages.success(self.request, 'Patient record created successfully!')
        return super().form_valid(form)


class PatientRecordUpdateView(LoginRequiredMixin, IsDoctorMixin, UpdateView):
    model = PatientRecord
    form_class = PatientRecordForm
    template_name = 'medical/patientrecord_form.html'
    success_url = reverse_lazy('patientrecord_list')

    def form_valid(self, form):
        messages.success(self.request, 'Patient record updated successfully!')
        return super().form_valid(form)


class AppointmentListView(LoginRequiredMixin, IsDoctorMixin, ListView):
    model = Appointment
    template_name = 'medical/appointment_list.html'
    context_object_name = 'appointments'
    paginate_by = 10

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user)


class AppointmentCreateView(LoginRequiredMixin, IsDoctorMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'medical/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        messages.success(self.request, 'Appointment created successfully!')
        return super().form_valid(form)


class AppointmentUpdateView(LoginRequiredMixin, IsDoctorMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'medical/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def form_valid(self, form):
        messages.success(self.request, 'Appointment updated successfully!')
        return super().form_valid(form)


# Admin Views
@login_required
def admin_dashboard(request):
    if request.user.user_type != 'admin':
        return redirect('dashboard')
    
    context = {
        'total_users': User.objects.count(),
        'total_patients': Patient.objects.count(),
        'total_doctors': User.objects.filter(user_type='doctor').count(),
        'total_appointments': Appointment.objects.count(),
        'recent_appointments': Appointment.objects.order_by('-created_at')[:5],
    }
    return render(request, 'medical/admin_dashboard.html', context)


class AdminPatientListView(LoginRequiredMixin, IsAdminMixin, ListView):
    model = Patient
    template_name = 'medical/admin_patient_list.html'
    context_object_name = 'patients'
    paginate_by = 10


class AdminIllnessListView(LoginRequiredMixin, IsAdminMixin, ListView):
    model = Illness
    template_name = 'medical/admin_illness_list.html'
    context_object_name = 'illnesses'
    paginate_by = 10


class AdminTreatmentListView(LoginRequiredMixin, IsAdminMixin, ListView):
    model = Treatment
    template_name = 'medical/admin_treatment_list.html'
    context_object_name = 'treatments'
    paginate_by = 10


class AdminPatientRecordListView(LoginRequiredMixin, IsAdminMixin, ListView):
    model = PatientRecord
    template_name = 'medical/admin_patientrecord_list.html'
    context_object_name = 'records'
    paginate_by = 10


class AdminAppointmentListView(LoginRequiredMixin, IsAdminMixin, ListView):
    model = Appointment
    template_name = 'medical/admin_appointment_list.html'
    context_object_name = 'appointments'
    paginate_by = 10
