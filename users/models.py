from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Custom user model inheriting from AbstractBaseUser and PermissionsMixin
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=50, default="Unknown")
    last_name = models.CharField(_("last name"), max_length=50, default="Unknown")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Set the email field as the username field for authentication
    USERNAME_FIELD = "email"
    # Specify additional fields required for user creation (besides email and password)
    REQUIRED_FIELDS = ["first_name", "last_name"]
    # The REQUIRED_FIELDS should match the fields you've defined in your CustomUserCreationForm.

    # Use the CustomUserManager to manage this model
    objects = CustomUserManager()

    def __str__(self):
        return self.email
