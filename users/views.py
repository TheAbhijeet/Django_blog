from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Define a view for user sign-up, inheriting from CreateView
class SignUp(generic.CreateView):
    # Use the CustomUserCreationForm for user registration
    form_class = CustomUserCreationForm
    # Redirect to the login page after successful registration
    success_url = reverse_lazy("login")
    # Use the 'signup.html' template for rendering the form
    template_name = "signup.html"

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

def logout_view(request):
    logout(request)
    return redirect('blog:home')  # Redirect to the desired page after logout, in case,here -> home
