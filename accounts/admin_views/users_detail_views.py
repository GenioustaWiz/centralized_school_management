from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver

from ..admin_forms.custom_user_assign_form import GroupAssignmentForm
from accounts.models import User

@login_required
#only users authorized to view users profile will get acces to this
@permission_required('auth.view_user', raise_exception=True) 
def user_detail(request, user_id):
    profile = get_object_or_404(User, id=user_id)
     # Combine first name and last name into a "Name" field
    full_name = f"{profile.first_name} {profile.last_name}" if profile.first_name or profile.last_name else "None"

    # Create a dictionary to hold the profile data with "None" for empty fields
    profile_data = {
        'Name': full_name, 
        'Email': profile.email,
        'Gender': profile.gender,
        'Phone Number': profile.phone_number,
        'IP Address': profile.ip_address,
        'Country': profile.country,
        'Description': profile.desc,
        
    }
    # Replace empty fields with "None"
    for key, value in profile_data.items():
        if not value:
            profile_data[key] = "None"
    # if request.method == 'POST':
    #     action = request.POST.get('action')
    #     print('====ACTION====')
    #     print(action)
    #     form = GroupAssignmentForm(request.POST,)
    #     if form.is_valid():
    #         # action = form.cleaned_data.get('action')
    #         group = form.cleaned_data.get('group')
    #         print('====ACTION22====')
    #         print(action)
    #         if action == 'save_group':
    #             user.groups.clear()  # Remove user from all groups
    #             user.groups.add(group)  # Add the selected group
    #             return redirect('user_detail', user_id=user.id)
    #         elif action == 'remove_group':
    #             user.groups.remove(group)  # Remove the selected group
    #             return redirect('user_detail', user_id=user.id)
    #         elif action == 'delete_user':
    #             # Delete the user and their profile
    #             user.delete()
    #             return redirect('user_list')  # Redirect to user list or another page after deletion

    # else:
    #     form = GroupAssignmentForm()
            
    context={
        'profile_data': profile_data,
        'profile': profile,
        # 'form': form,
        }
    return render(request, 'maindashboard/users_admin/user_detail2.html', context)

@login_required
#only users authorized to view users profile will get acces to this
@permission_required('auth.view_user', raise_exception=True) 
def user_edit(request, user_id):
    profile = get_object_or_404(User, id=user_id)
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        print('====ACTION====')
        print(action)
        form = GroupAssignmentForm(request.POST,)
        if form.is_valid():
            # action = form.cleaned_data.get('action')
            group = form.cleaned_data.get('group')
            print('====ACTION22====')
            print(action)
            # Get the ContentType for the User model
            user_content_type = ContentType.objects.get_for_model(User)
            # Print the content_type_id
            print(user_content_type.id)
            # Log the user activity using LogEntry
            if action == 'save_group':
                action_flag = CHANGE  # Use CHANGE for modifications
                content_type_id = user_content_type.id
            elif action == 'remove_group':
                action_flag = CHANGE  # Use CHANGE for modifications
                content_type_id = user_content_type.id
            elif action == 'delete_user':
                action_flag = DELETION
                content_type_id = user_content_type.id
            else:
                action_flag = ADDITION
            LogEntry.objects.create(
                user_id=request.user.id,
                content_type_id=content_type_id,  # You can replace with the actual content type ID if applicable
                object_id=user_id,
                object_repr=str(user),
                action_flag=action_flag,
            )
            if action == 'save_group':
                user.groups.clear()  # Remove user from all groups
                user.groups.add(group)  # Add the selected group
                return redirect('user_detail', user_id=user.id)
            elif action == 'remove_group':
                user.groups.remove(group)  # Remove the selected group
                return redirect('user_detail', user_id=user.id)
            elif action == 'delete_user':
                # Delete the user and their profile
                user.delete()
                return redirect('user_list')  # Redirect to user list or another page after deletion

    else:
        form = GroupAssignmentForm()
            
    context={
        'profile': profile,
        'form': form,
        }

    return render(request, 'maindashboard/users_admin/user_edit_group.html', context)


def custom_admin_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Check if 'groups' or 'user_permissions' are present in request.POST
        if 'groups' in request.POST:
            group_ids = request.POST.getlist('groups')
            # Add the user to the selected groups
            user.groups.set(group_ids)
        elif 'user_permissions' in request.POST:
            permission_ids = request.POST.getlist('user_permissions')
            # Assign the selected permissions to the user
            user.user_permissions.set(permission_ids)

    groups = Group.objects.all()
    permissions = Permission.objects.all()

    context = {
        'user': user,
        'groups': groups,
        'permissions': permissions,
    }

    return render(request, 'maindashboard/users_admin/user_edit_group.html', context)
