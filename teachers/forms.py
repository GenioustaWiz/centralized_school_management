from django import forms 
from .models import Teacher

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = [ 'schools', 'qualifications', 'subjects'] 