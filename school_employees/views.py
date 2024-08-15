# school_employees/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms.forms import SchoolEmployeeForm
from .models import SchoolEmployee
from .serializers import SchoolEmployeeSerializer

def school_employee_form(request):
    if request.method == 'POST':
        form = SchoolEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or list view
    else:
        form = SchoolEmployeeForm()
    
    return render(request, 'school_employees/school_employee_form.html', {'form': form})

# For API ACCESS
@api_view(['GET', 'POST'])
def school_employee_api(request):
    if request.method == 'GET':
        employees = SchoolEmployee.objects.all()
        serializer = SchoolEmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SchoolEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
