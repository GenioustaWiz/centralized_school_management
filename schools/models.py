# schools/models.py
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    school_type = models.CharField(max_length=20, choices=(('public', 'Public'), ('private', 'Private')))
    education_levels = models.JSONField()  # Store multiple selections as JSON
