# views.py

from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from users.models import User   # Import the User model if not already imported
from django.shortcuts import render

def recent_activities(request):
     # Get the superuser (admin) user object
    superuser = User.objects.get(username='admin')  # Replace 'admin' with the superuser's username
    # Filter out actions by the superuser
    recent_activities = LogEntry.objects.exclude(user=superuser).order_by('-action_time')[:10]
    
    # without filtering out the super user
    # recent_activities = LogEntry.objects.order_by('-action_time')[:10]  # Get the last 10 log entries

    return render(request, 'admin/recent_activities.html', {'log_entries': recent_activities})
