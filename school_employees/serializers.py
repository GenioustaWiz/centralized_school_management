# school_employees/serializers.py

from rest_framework import serializers
from .models import SchoolEmployee

class SchoolEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolEmployee
        fields = ['id', 'user', 'school', 'department', 'qualifications']
