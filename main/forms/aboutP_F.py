from django import forms
from users.models import User 
from tinymce.widgets import TinyMCE
from ..models.aboutP_M import AboutPage, AboutList


class AboutPageForm(forms.ModelForm):
    body =  forms.CharField(widget=TinyMCE ()) #tinymce Editor.
    class Meta:
        model = AboutPage
        fields = ['heading', 'body']

# class AboutListForm(forms.ModelForm):
#     class Meta:
#         model = AboutList
#         fields = ['title', 'image', 'desc']

# from users.models import Profile
class AboutListForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AboutListForm, self).__init__(*args, **kwargs)
    
    #     # Filter users with is_staff=True
    #     self.fields['user'].queryset = Profile.objects.filter(user__is_staff=True)
    class Meta:
        model = AboutList
        fields = ['user','title', 'image', 'desc'] 
