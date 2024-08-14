# administration/models.py

from django.db import models
from accounts.models import User

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    qualifications = models.TextField()
    # Add other relevant fields