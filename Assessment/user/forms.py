# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserAccount

class RegistrationForm(UserCreationForm):
    """
    Custom registration form for creating new user accounts.
    """
    class Meta:
        model = UserAccount
        fields = ['name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

class CustomLoginForm(AuthenticationForm):
    """
    Custom login form for user authentication.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
