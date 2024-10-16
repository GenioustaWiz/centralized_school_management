
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required 

from teachers.models import Teacher
from accounts.models import User  
from students.models import Student, Attendance, Performance

def teacher_A_list(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/p_t_a_universal/list.html'
            
        else:
            template_name = 'teacher/teacher_list.html'
    else:
        template_name = 'teacher/teacher_list.html'

    teachers = Teacher.objects.all()

    context = {
        'context_list': teachers,
        'title': 'Teachers',
    }

    return render(request, template_name, context)
@login_required
def teacher_A_detail(request, pk=None):

    # Check the user's type, for access limitations 
    if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
        template_name = 'maindashboard/p_t_a_universal/details.html' 
    else: template_name = 'forbidden.html' 
    
    teacher = get_object_or_404(Teacher, pk=pk) 
    user = teacher.user
    context = { 
               'context_details': teacher, 
                'title': (f'{user.first_name} Details' ),
               } 
    return render(request, template_name, context) 