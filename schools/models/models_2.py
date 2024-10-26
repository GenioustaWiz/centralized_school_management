
from django.db import models
from django.utils.text import slugify
from django.db.models import Sum, Count
from schools.models.models import School

class SchoolPerformance(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_graduates = models.IntegerField()
    college_acceptance_rate = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        ordering = ['-year']

class SchoolActivity(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'School Activities'

class Award(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_received = models.DateField()
    awarding_body = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-date_received']