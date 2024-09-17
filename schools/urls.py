# school_employees/urls.py

from django.urls import path
from .admin_views.school_A_views import *
from .views import *

urlpatterns = [
    
    path('schools/', school_list, name='school_list'),
    path('<slug:slug>/school/', school_detail, name='school_detail'),
    path('schools/add/', edit_add_school, name='edit_add_school'),
    path('schools/edit/<int:pk>/', edit_add_school, name='edit_add_school'),
    path('schools/delete/<int:pk>/', school_delete, name='school_delete'),

    path('api/school/', SchoolAPIView.as_view(), name='school_api_views'),

    # path('form/', SchoolFormView, name='SchoolFormView'),
    
] 
    