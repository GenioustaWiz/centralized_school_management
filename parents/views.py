
from django.shortcuts import render, redirect, get_object_or_404
from parents.models import Parent
from accounts.models import User  

def parent_list(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/parent/parent_list.html'
            
        else:
            template_name = 'parent/parent_list.html'
    else:
        template_name = 'parent/parent_list.html'

    parents = Parent.objects.all()

    context = {
        'parents': parents,
    }

    return render(request, template_name, context)

def parent_detail(request, pk):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/parent/parent_details.html'
        else:
            template_name = 'parent/parent_details.html'
    else:
        template_name = 'parent/parent_details.html'

    parent = get_object_or_404(Parent, pk=pk)

    context = {
        'parent': parent,
    }

    return render(request, template_name, context)

