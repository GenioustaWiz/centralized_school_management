# students/models.py
from django.db import models
from accounts.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('parents.Parent', on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=10)
    # Add other relevant fields
