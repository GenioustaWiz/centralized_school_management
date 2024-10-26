
from django.db import models
from django.utils import timezone
from accounts.models import User
from schools.models.models import School

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

class Event(models.Model):
    EVENT_TYPES = [
        ('academic', 'Academic'),
        ('sports', 'Sports'),
        ('cultural', 'Cultural'),
        ('other', 'Other')
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    is_recurring = models.BooleanField(default=False)
    registration_required = models.BooleanField(default=False)
    max_participants = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['start_date']