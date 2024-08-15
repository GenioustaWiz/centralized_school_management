# teachers/models.py

from django.db import models
from accounts.models import User
from schools.models import School

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Add association with School
    qualifications = models.TextField()
    subjects = models.JSONField()  # Store multiple subjects as JSON

    def __str__(self):
        return f"{self.user} - {self.school}"

