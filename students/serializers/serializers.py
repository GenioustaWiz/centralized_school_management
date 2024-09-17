from rest_framework import serializers
from students.models import Student, Attendance, Performance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'parent', 'first_name', 'middle_name', 'last_name', 'gender', 'birth_date', 'Emergency_contact', 'rfid_tag', 'school', 'school_identification']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status']

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['id', 'student', 'subject', 'grade', 'assessment_date']