# school_employees/models.py

from django.db import models
from accounts.models import User
from schools.models import School

class SchoolEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    qualifications = models.TextField()
    

    def __str__(self):
        return f"{self.user} - {self.department}"
