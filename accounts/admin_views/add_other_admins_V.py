
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from ..admin_forms.add_other_admins_F import AdminRegistrationForm
from accounts.models import User
from ..utils.decorators import user_type_required

# @user_passes_test(is_superuser)
@user_type_required('master_admin', 'lead_admin', 'data_admin')
def register_admins(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = form.cleaned_data['user_type']
            user.set_password("1234")  # Set the default password
            user.save()
            return redirect('user_list')  # Redirect to admin dashboard or another appropriate page
    else:
        form = AdminRegistrationForm()
    context = {
    'form': form,
    'title': 'Register Admin'
    }
    return render(request, 'maindashboard/users_admin/add_users/add_other_users.html', context)

