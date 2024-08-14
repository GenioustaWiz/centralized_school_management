from django import forms
from ..models.models import BaseData

class BaseDataForm(forms.ModelForm):
    class Meta:
        model = BaseData
        fields = ['logo_img', 'logo_name', 'footer']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance