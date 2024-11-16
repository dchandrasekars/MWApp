from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    empno = models.CharField(max_length=10, unique=True)  # Employee number
    ename = models.CharField(max_length=100)             # Employee name
    section = models.CharField(max_length=50)            # Section or department
    phone = models.CharField(max_length=15, blank=True, null=True)