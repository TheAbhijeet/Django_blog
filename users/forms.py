from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django import forms

# Custom form for creating new users, inheriting from UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        # Specify the fields to be displayed and filled in the form
        fields = ("email", "first_name", "last_name")
        # Add placeholder attributes for the email input field
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Email address"}),
        }
    
    # Define individual form fields with placeholder attributes
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': "First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': "Last name"}))

# Custom form for editing user details, inheriting from UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Specify the fields to be displayed and edited in the form
        fields = ("email",)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
