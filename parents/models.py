# parents/models.py
from django.db import models
from accounts.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other relevant fields
