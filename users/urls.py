from django.urls import path
from . import views
from .views import CustomLoginView

# Set the app name for namespacing the URLs
app_name = 'users'

# Define the URL patterns for the 'users' app
urlpatterns = [
    # URL pattern for the 'signup' view
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('login/', CustomLoginView.as_view(), name='login'),
    # Logout user
    path('logout/', views.logout_view, name='logout'),
]
