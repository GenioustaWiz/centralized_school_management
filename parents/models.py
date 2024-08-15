from django.db import models
from accounts.models import User
from schools.models import School

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schools = models.ManyToManyField(School, blank=True)  # Allow association with multiple schools
    # Add other relevant fields

    def __str__(self):
        return str(self.user)
