from rest_framework import serializers
from students.models import Student

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'school_identification', 'student_number']
