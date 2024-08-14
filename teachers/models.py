# teachers/models.py
from django.db import models
from accounts.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualifications = models.TextField()
    subjects = models.JSONField()  # Store multiple subjects as JSON
    