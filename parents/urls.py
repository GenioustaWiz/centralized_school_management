
from django.urls import path
from .admin_views.parents_A_views import *
from .views import *

urlpatterns = [
    
    path('parents/', parent_list, name='parent_list'),
    path('parent/details', parent_detail, name='parent_detail'),
    path('parent/add/', edit_add_parent, name='edit_add_parent'),
    path('parent/edit/<int:pk>/', edit_add_parent, name='edit_add_parent'),
    path('parent/delete/<int:pk>/', parent_delete, name='parent_delete'),

    # ========= For APIViews ============
    path('api/parent/', ParentAPIView.as_view(), name='parent_api_views'),
]
