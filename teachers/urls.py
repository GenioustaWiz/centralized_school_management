
from django.urls import path
from .admin_views.teachers_A_views import *
from .admin_views.views import *

urlpatterns = [
    
    # path('Your-Dashboard/', teacher_detail, name='teacher_detail'),
    path('teachers/', teacher_A_list, name='teacher_A_list'),

    path('teacher/details/<int:pk>/', teacher_A_detail, name='teacher_A_detail'),
    # path('student/dashboard/<int:pk>/', student_dashboard, name='student_dashboard'),
    
    path('teacher/add/', teacher_register_edit, name='teacher_register_edit'),
    path('teacher/edit/<int:pk>/', teacher_register_edit, name='teacher_register_edit'),
    path('teacher/delete/<int:pk>/', teacher_delete, name='teacher_delete'),
    # ========= For APIViews ============
    # path('api/teacher/', ParentAPIView.as_view(), name='teacher_api_views'),
]
