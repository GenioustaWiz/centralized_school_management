from django.shortcuts import render, redirect

from .models.models import *
from .models.aboutP_M import *
def main_index(request):

    # Render the response and send it back!
    return render(request, 'index.html')