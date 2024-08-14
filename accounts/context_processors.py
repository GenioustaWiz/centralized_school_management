# yourapp/context_processors.py

# Add this context processor to your Django settings
# templates:
#            Options:
#                    'context_processors':[
#                         'yourapp.context_processors.user_profile',
#                     ]

from .models import User  # Replace with the actual import path for your User model

def user_info(request):
    # Assuming your User model is associated with the request
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
    else:
        user = None

    return {'user_info': user}