# from turtle import textinput
from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

# class loginpage(forms.Form):
#     username = forms.CharField(max_length=63)
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput)

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() 

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'username',]
        widgets = {
            'email': EmailInput(attrs={
                'class': "email", 
                'placeholder': 'Email'
                })
        }

class ProfileUpdateForm_c(forms.ModelForm):
    phone_number = PhoneNumberField(
            widget=PhoneNumberPrefixWidget(initial='KE', attrs={'class': 'p-no'})
        ) 
    class Meta:
        model = User
        fields = ['phone_number','country']
# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['gender','image','github','facebook','googleplus','instagram', ]
           
    
# Create a ProfileUpdateForm to update image
class ProfileUpdateForm_desc(forms.ModelForm):
    class Meta:
        model = User
        fields =['desc']