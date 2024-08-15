# school_employees/forms.py

from django import forms
from .models import SchoolEmployee
from accounts.models import User
from schools.models import School

class SchoolEmployeeForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    school = forms.ModelChoiceField(queryset=School.objects.all(), required=True)
    department = forms.CharField(max_length=100, required=True)
    qualifications = forms.CharField(widget=forms.Textarea, required=True)
    
    class Meta:
        model = SchoolEmployee
        fields = ['user', 'school', 'department', 'qualifications']
        
