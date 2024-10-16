
from django.urls import path
from .admin_views.parents_A_views import *
from .admin_views.views import *
from .views.views import *

urlpatterns = [
    
    path('Your-Dashboard/', parent_detail, name='parent_detail'),
    path('parents/', parent_A_list, name='parent_A_list'),

    path('parent/details/<int:pk>/', parent_A_detail, name='parent_A_detail'),
    # path('student/dashboard/<int:pk>/', student_dashboard, name='student_dashboard'),
    
    path('parent/add/', parent_register_edit, name='parent_register_edit'),
    path('parent/edit/<int:pk>/', parent_register_edit, name='parent_register_edit'),
    path('parent/delete/<int:pk>/', parent_delete, name='parent_delete'),
    # ========= For APIViews ============
    # path('api/parent/', ParentAPIView.as_view(), name='parent_api_views'),
]
