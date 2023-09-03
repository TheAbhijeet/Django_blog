from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Define a custom admin class for the CustomUser model
class CustomUserAdmin(UserAdmin):
    # Use the CustomUserCreationForm for adding users
    add_form = CustomUserCreationForm
    # Use the CustomUserChangeForm for editing users
    form = CustomUserChangeForm
    # Use the CustomUser model for managing users
    model = CustomUser
    # Display these fields in the list view of admin
    list_display = ("email", "is_staff", "is_active",)
    # Add filters for these fields in the list view
    list_filter = ("email", "is_staff", "is_active",)
    # Define the fieldsets for editing user details
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    # Define the fieldsets for adding users
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    # Enable searching users by email
    search_fields = ("email",)
    # Set the default ordering for the list view
    ordering = ("email",)

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
