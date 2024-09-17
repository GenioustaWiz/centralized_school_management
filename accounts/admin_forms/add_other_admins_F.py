# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class AdminRegistrationForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPES)

    class Meta:
        model = User
        fields = ('user_type', 'email', 'first_name', 'last_name', 'phone_number', 'image', 'gender', )
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password'].help_text = 'Enter a strong password for the Master Admin.'
