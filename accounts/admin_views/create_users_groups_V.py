from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import Permission, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..admin_forms.add_group_forms import *

def group_list_view(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        action = request.POST.get('action', '')
        selected_group_ids = request.POST.getlist('_selected_action')

        if action == 'delete_selected':
            Group.objects.filter(pk__in=selected_group_ids).delete()
            messages.success(request, 'Selected groups deleted successfully.')

            # Redirect to the same view after the action
            return redirect('group_list')
    # Set the number of groups to display per page
    items_per_page = 7
    paginator = Paginator(groups, items_per_page)

    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)

    context = {'groups': groups}

    return render(request, 'maindashboard/users_admin/groups/group_list.html', context)
    
def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    queryset=group.permissions.all()
    print("this group permissions:", queryset)

    context={
        'group': group,
        'permissions': queryset,  # Pass the queryset to the context
        }
    return render(request, 'maindashboard/users_admin/groups/group_detail.html', context)
def add_group_(request):
    if request.method == 'POST':
        print("check if permission")
        form = GroupForm(request.POST)
        permission_form = Permission_Form(request.POST)
        # Access the entire select element and its options
        # selected_permissions_select = request.POST.get('select_permissions')
        # print(selected_permissions_select)  # Add this line for debugging

        selected_permissions = GroupPermissionForm(request.POST)
        print("Selected Permissions:", selected_permissions)

        if form.is_valid() :
            group = form.save()
            print("group;", group)
            # Get the Permission objects based on the selected IDs
            # permissions = Permission.objects.filter(id__in=selected_permission_ids)
            # # Set the permissions for the group
            # group.permissions.set(permissions)
            
            print("check if permission22")
            print(permissions)
            return redirect('user_list')  # Change 'group_list' to the actual URL name for your group list view

    else:
        form = GroupForm()
        permission_form = Permission_Form()
        selected_permissions = GroupPermissionForm()
    context = {
        'form': form, 
        'permission_form': permission_form,
        'selectpermission_form': selected_permissions,
    }
    return render(request, 'maindashboard/users_admin/groups/add_group.html', context)

    # Add this return statement for non-POST requests
    # return HttpResponse("This is a non-POST request response.")

def add_group(request, pk=None):
    if pk is not None:
        group = get_object_or_404(Group, pk=pk)
        queryset=group.permissions.all()
        form = GroupForm(instance=group)
        print("this group permissions:", queryset)
        initial_permissions = group.permissions.values_list('id', flat=True)
        selected_permissions = SelectPermissionForm(queryset=queryset, initial={'permissions': initial_permissions})
    else:
        group = None
        form = GroupForm()
        
        selected_permissions = SelectPermissionForm()

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)

        if form.is_valid():
            group = form.save()
            # Handle permissions
            selected_permission_ids = request.POST.getlist('select_permissions')
            print("this selected_permission_ids:", selected_permission_ids)
            permissions = Permission.objects.filter(id__in=selected_permission_ids)
            group.permissions.set(permissions)

            return redirect('group_list')  # Change 'user_list' to the actual URL name for your user list view

    permission_form = GroupPermissionForm()

    context = {
        'form': form,
        'permission_form': permission_form,
        'selectpermission_form': selected_permissions,
    }

    return render(request, 'maindashboard/users_admin/groups/add_group.html', context)