from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from accounts.models import User
from ..admin_forms.custom_user_assign_form import GroupAssignmentForm

@login_required
@user_passes_test(lambda user: user.groups.filter(name='moderator').exists())
def assign_user_group(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = GroupAssignmentForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            user.groups.clear()  # Remove user from all groups
            user.groups.add(group)  # Add the selected group
            return redirect('profile_detail', user_id=user.id)
        
    else:
        form = GroupAssignmentForm()

    return render(request, 'maindashboard/users_admin/assign_user_group.html', {'form': form, 'user': user})
