from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'user_type', 'phone', 'address', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user
