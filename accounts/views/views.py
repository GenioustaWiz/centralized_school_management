from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from accounts.models import User
# Import User UpdateForm, ProfileUpdatForm
from accounts.forms import *

from django.views.generic import TemplateView, View
from allauth.account.views import LogoutView

# Create your views here.
def home(request):
    return render(request, 'home.html',)

# Update it here
@login_required
def profile(request):
    user = request.user

    # Check if a profile exists for the user, or create one if it doesn't exist
    profile, created = User.objects.get_or_create(email=user.email)

    full_name = f"{profile.first_name} {profile.last_name}" if profile.first_name or profile.last_name else "None"

    profile_data = {
        'Name': full_name,
        'Email': profile.email,
        'Gender': profile.gender,
        'Phone Number': profile.phone_number,
    }

    # Replace empty fields with "None"
    for key, value in profile_data.items():
        if not value:
            profile_data[key] = "None"

    context = {
        'profile_data': profile_data,
        'profile': profile,
    }

    return render(request, 'profile/profile_view.html', context)

@login_required
def profile_edit( request):
    user = request.user
    # Check if a profile exists for the user, or create one if it doesn't exist
    profile, created = User.objects.get_or_create(email=user.email)
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=profile)
    #     c_form= ProfileUpdateForm_c(request.POST,instance=profile) #for proccessing phone_number and country selectoptions
    #     p_form = ProfileUpdateForm(request.POST,
    #                                request.FILES,
    #                                instance=profile) 
        
    #     desc_form =  ProfileUpdateForm_desc(request.POST, instance=profile)
    #     if u_form.is_valid() and p_form.is_valid() and desc_form.is_valid() and c_form.is_valid:
    #         u_form.save()
    #         p_form.save() 
    #         # phone_number = c_form.phone_number
    #         # print("=========c-form===========")
    #         # print(phone_number)
    #         # print(country)
    #         c_form.save()  
    #         profile.save()
    #         desc_form.save()  # Save the description form
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile') # Redirect back to profile page

    # else:
    #     u_form = UserUpdateForm(instance=profile)
    #     c_form = ProfileUpdateForm_c(instance=profile)
    #     p_form = ProfileUpdateForm(instance=profile)
    #     desc_form =  ProfileUpdateForm_desc(instance=profile)
    
    context = {
        # 'u_form': u_form,
        # 'c_form': c_form,
        # 'p_form': p_form,
        # 'desc_form': desc_form,
        'profile': profile,
    }

    return render(request, 'profile/profile_edit.html', context) 

# called from users profile view
class DeleteAccountView(TemplateView):
    template_name = 'account/delete_account_confirm.html'
   
    def post(self, request, *args, **kwargs):
        
        # Add logic to handle account deletion here
        # Add additional logic to delete the user account
        request.user.delete()

        messages.success(request, 'Your account has been deleted.')
        return redirect("home")  