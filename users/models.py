from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    text_password = models.CharField(max_length=128, null=True, blank=True)
