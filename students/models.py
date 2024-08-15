# students/models.py

from django.db import models
from accounts.models import User
from schools.models import School
from parents.models import Parent

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    # Add other relevant fields

    def __str__(self):
        return f"{self.user} - {self.grade}"
