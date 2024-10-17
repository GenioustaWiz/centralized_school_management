# yourapp/context_processors.py

# Add this context processor to your Django settings
# templates:
#            Options:
#                    'context_processors':[
#                         'yourapp.context_processors.user_profile',
#                     ]

from schools.models.models import School  # Replace with the actual import path for your User model

def school_info(request):
    # Assuming your User model is associated with the request
    if request.user.is_authenticated:
        school = School.objects.get()
    else:
        school = None

    return {'school_info': school}