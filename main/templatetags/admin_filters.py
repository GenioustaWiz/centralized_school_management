from django import template
from django.contrib.admin.models import LogEntry

register = template.Library()

ACTION_CHOICES = {
    1: 'Add',
    2: 'Change',
    3: 'Delete',
    4: 'View',  # For viewing an object without making changes
    5: 'Login',  # For user login actions
    6: 'Logout',  # For user logout actions
}

@register.filter
def display_action(action_flag):
    return ACTION_CHOICES.get(action_flag, action_flag)
