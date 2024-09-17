from django import forms
from django.contrib.auth.models import Group

class GroupAssignmentForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
