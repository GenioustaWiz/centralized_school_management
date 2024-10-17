
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum
from django.contrib import messages

from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from accounts.models import User   # Import the User model if not already imported
from django.shortcuts import render

from parents.models import Parent
from schools.models.models import School 

@login_required
def school_dashboard_home(request):
    
    total_parents, total_schools = Parent.get_total_parents_and_schools()
    parents_combined_data = [total_parents, total_schools]
    total_schools, total_types = School.get_total_schools_and_types()
    schools_combined_data = [total_schools, total_types]

    # total_visitors, total_visits = Visit.get_total_visitors_and_visits()
    
    # Get the superuser (admin) user object
    # superuser = User.objects.get(username='admin')  # Replace 'admin' with the superuser's username
    # Filter out actions by the superuser
    # recent_activities = LogEntry.objects.exclude(user=superuser).order_by('-action_time')[:10]
    
    # without filtering out the super user
    recent_activities = LogEntry.objects.order_by('-action_time')[:20]  # Get the last 10 log entries

    context = { 
        'total_parents': total_parents,
        'total_schools': total_schools,
        'schools_combined_data': schools_combined_data,

        # 'total_visitors': total_visitors,
        # 'total_visits': total_visits,
        'log_entries': recent_activities,
    }
    return render(request, 'school/dashboard/dashboard_home.html', context)
    # Allow staff members (admin) to access this view
@staff_member_required
def dashboard_home_admin(request):
    return main_dashboard_home(request)