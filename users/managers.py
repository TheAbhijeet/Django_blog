from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        
        # Normalize the email address (convert domain part to lowercase)
        email = self.normalize_email(email)
        
        # Create a user instance with the provided fields
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Set the user's password securely
        user.save()  # Save the user object to the database
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        # Ensure the required fields are set for a superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Check that is_staff and is_superuser are True for a superuser
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        # Call the create_user method to create the superuser
        return self.create_user(email, password, **extra_fields)
