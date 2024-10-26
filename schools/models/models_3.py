
from django.db import models
from django.utils import timezone
from schools.models.models import School
from students.models import Student
from teachers.models import Teacher


class StudentAchievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_achieved = models.DateField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date_achieved']

class FacultyHighlight(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    achievements = models.TextField()
    image = models.ImageField(upload_to='faculty/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    date_featured = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_featured']

class GalleryAlbum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']

class GalleryImage(models.Model):
    album = models.ForeignKey(GalleryAlbum, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']