from django.shortcuts import render
from ..models import User

def user_list(request):
    profiles = User.objects.all()
    return render(request, 'maindashboard/users_admin/users_list.html', {'profiles': profiles})
