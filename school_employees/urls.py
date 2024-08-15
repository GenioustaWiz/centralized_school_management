# school_employees/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.school_employee_form, name='school_employee_form'),
    path('api/school_employees/', views.school_employee_api, name='school_employee_api'),
]