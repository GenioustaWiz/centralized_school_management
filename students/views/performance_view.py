
from django.shortcuts import render, redirect, get_object_or_404
from students.models import Performance
from accounts.models import User

def performance_list(request):
    # check if the user is Authenticated
    if request.user.is_authenticated:
        # check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/student/performance/performance_list.html'
        else:
            template_name = 'student/performance/performance_list.html'
        performances = Performance.objects.all()
        context = {
            'performances': performances
        }
        return render(request, template_name, context)

def performance_detail(request):
    # check if the user is Authenticated
    if request.user.is_authenticated:
        # check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/student/performance/performance_detail.html'
        else:
            template_name = 'student/performance/performance_detail.html'
        performance = Performance.objects.all()
        context = {
            'performance_detail': performance,
        }
        return render(request, template_name, context)

    