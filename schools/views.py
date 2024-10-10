
from django.shortcuts import render, redirect, get_object_or_404
from schools.models.models import School
from accounts.models import User  

def school_list(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/school/school_list.html'
            
        else:
            template_name = 'school/school_list.html'
    else:
        template_name = 'school/school_list.html'

    schools = School.objects.all()

    context = {
        'schools': schools,
    }

    return render(request, template_name, context)

def school_detail(request, slug):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check the user's type, for access limitations
        if request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/school/school_details.html'
        else:
            template_name = 'school/school_details.html'
    else:
        template_name = 'school/school_details.html'

    school = get_object_or_404(School, slug=slug)

    context = {
        'school_detail': school,
    }

    return render(request, template_name, context)

