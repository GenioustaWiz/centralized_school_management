from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum
from django.contrib import messages

from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from accounts.models import User   # Import the User model if not already imported
from django.shortcuts import render

# from visitors_counter.models import Visit
@login_required
def main_dashboard_home(request):
    
    # total_visitors, total_visits = Visit.get_total_visitors_and_visits()
    
    # Get the superuser (admin) user object
    # superuser = User.objects.get(username='admin')  # Replace 'admin' with the superuser's username
    # Filter out actions by the superuser
    # recent_activities = LogEntry.objects.exclude(user=superuser).order_by('-action_time')[:10]
    
    # without filtering out the super user
    recent_activities = LogEntry.objects.order_by('-action_time')[:20]  # Get the last 10 log entries

    context = {
        # 'total_visitors': total_visitors,
        # 'total_visits': total_visits,
        'log_entries': recent_activities
    }
    return render(request, 'maindashboard/dashboard_home.html', context)
    # Allow staff members (admin) to access this view
@staff_member_required
def dashboard_home_admin(request):
    return main_dashboard_home(request)