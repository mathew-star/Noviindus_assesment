# user/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm,CustomLoginForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
User = get_user_model()

def register(request):
    """
    View for handling user registration.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'user/register.html',{'form': form})

class CustomLoginView(LoginView):
    """
    Custom login view using the AuthenticationForm.
    """
    authentication_form = CustomLoginForm
    template_name = 'user/login.html'
    
    
    def get_success_url(self):
        """
        Redirect to the home page after a successful login.
        """
        return reverse('home') 

    def form_valid(self, form):
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login failed. Please check your email and password.')
        return super().form_invalid(form)

class HomePageView(LoginRequiredMixin, TemplateView):
    """
    View for the home page.
    """
    template_name = 'user/Hompage.html'
    login_url = '/login/'  # Redirect to the login page if the user is not authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_data'] = {
            'username': user.name,
            'email': user.email,
        }
        return context
