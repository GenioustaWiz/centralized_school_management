from django import forms
from .models import Student, Attendance, Performance

class StudentForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'b-date', 'placeholder': 'YYYY-MM-DD'}
        )
    )
    class Meta:
        model = Student
        fields = ['parent', 'first_name', 'middle_name', 'last_name', 'gender', 'birth_date', 'Emergency_contact', 'rfid_tag', 'school', 'school_identification']

class AttendanceForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'date', 'placeholder': 'YYYY-MM-DD'}
        )
    )
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']

class PerformanceForm(forms.ModelForm):
    assessment_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'date', 'placeholder': 'YYYY-MM-DD'}
        )
    )
    class Meta:
        model = Performance
        fields = ['student', 'subject', 'grade', 'assessment_date']

