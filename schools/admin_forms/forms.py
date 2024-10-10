
from django import forms
from django import forms
from schools.models.models import  School, SchoolContactInfo
from schools.models.education_m import EducationStage, EducationLevel

class EducationStageForm(forms.ModelForm):
    class Meta:
        model = EducationStage
        fields = ['name']

class EducationLevelForm(forms.ModelForm):
    class Meta:
        model = EducationLevel
        fields = ['name', 'stage', 'curriculum', 'has_sne', 'order']

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'location', 'school_type', 'education_levels', 'established_date', 'about', 'capacity']
        widgets = {
            'established_date': forms.DateInput(attrs={'type': 'date'}),
            'education_levels': forms.CheckboxSelectMultiple(),
        }

class SchoolContactInfoForm(forms.ModelForm):
    class Meta:
        model = SchoolContactInfo
        fields = ['phone_number', 'email', 'address', 'whatsapp']