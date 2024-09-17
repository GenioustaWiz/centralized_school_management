
from rest_framework import serializers
from .models import Parent

class ParentSerializer(serializers.ModelSerializer):
    class META:
        model = Parent
        fields = ['id', 'user', 'schools',]