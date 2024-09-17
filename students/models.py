# students/models.py

from django.db import models
from django.utils.crypto import get_random_string
from django.db.models import Sum, Count
from phonenumber_field.modelfields import PhoneNumberField

from schools.models import School
from parents.models import Parent

class Student(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'), 
        ('O', 'Other'),
    ]
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=gender_choices)
    birth_date = models.DateField(null=True, blank=True)
    Emergency_contact = PhoneNumberField(null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    school_identification = models.CharField(max_length=20, unique=True)
    student_number = models.CharField(max_length=10, unique=True, editable=False)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True)
    rfid_tag = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()
    
    def save(self, *args, **kwargs):
        if not self.student_number:
            self.student_number = self.generate_unique_student_number()
        super(Student, self).save(*args, **kwargs)
    
    def generate_unique_student_number(self):
        while True:
            random_number = get_random_string(8, allowed_chars='0123456789')
            if not Student.objects.filter(student_number=random_number).exists():
                return random_number

class Attendance(models.Model):
    status_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Excused', 'Excused'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    # date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=status_choices)
    
    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    grade = models.FloatField()
    assessment_date = models.DateField()
    # entry_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}- {self.assessment_date}"
