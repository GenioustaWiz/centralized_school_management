from django import forms
from ..models.models import HomePage, programming_languages

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['heading',] #removed 'body'

class ProgrammingLanguagesForm(forms.ModelForm):
    class Meta:
        model = programming_languages
        fields = ['PL_name', 'no_of_projects', 'PL_display_color', 'PL_image_logo']
