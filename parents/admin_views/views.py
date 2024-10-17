
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required 

from parents.models import Parent
from accounts.models import User  
from students.models import Student, Attendance, Performance

@login_required
def parent_A_list(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'school/dashboard/p_t_a_universal/list.html'
            
        else:
            template_name = 'parent/parent_list.html'
    else:
        template_name = 'parent/parent_list.html'

    parents = Parent.objects.all()

    context = {
        'context_list': parents,
        'title': 'Parents',
        'url_first': 'parent',
    }

    return render(request, template_name, context)
@login_required
def parent_A_detail(request, pk=None):

    # Check the user's type, for access limitations 
    if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
        template_name = 'school/dashboard/p_t_a_universal/details.html' 
    else: template_name = 'forbidden.html' 
    
    parent = get_object_or_404(Parent, pk=pk) 
    user = parent.user
    context = { 
               'context_details': parent, 
                'title': (f'{user.first_name} Details' ),
               } 
    return render(request, template_name, context) 