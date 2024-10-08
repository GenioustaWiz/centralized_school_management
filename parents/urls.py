
from django.urls import path
from .admin_views.parents_A_views import *
from .admin_views.views import *
from .views.views import *

urlpatterns = [
    
    path('parents/', parent_A_list, name='parent_A_list'),
    path('parent/details', parent_A_detail, name='parent_A_detail'),
    path('Your-Dashboard/', parent_detail, name='parent_detail'),
    # path('student/dashboard/<int:pk>/', student_dashboard, name='student_dashboard'),
    
    path('parent/add/', edit_add_parent, name='edit_add_parent'),
    path('parent/edit/<int:pk>/', edit_add_parent, name='edit_add_parent'),
    path('parent/delete/<int:pk>/', parent_delete, name='parent_delete'),
    # ========= For APIViews ============
    path('api/parent/', ParentAPIView.as_view(), name='parent_api_views'),
]
