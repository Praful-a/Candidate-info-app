from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile inside our system."""
