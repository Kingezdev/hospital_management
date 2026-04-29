from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from .models import User


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'admin':
            return '/medical/admin/dashboard/'
        elif user.user_type == 'doctor':
            return '/medical/doctor/dashboard/'
        return '/'


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    if user.user_type == 'admin':
        return redirect('admin_dashboard')
    elif user.user_type == 'doctor':
        return redirect('doctor_dashboard')
    return render(request, 'accounts/dashboard.html')
