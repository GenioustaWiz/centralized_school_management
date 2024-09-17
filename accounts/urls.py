from django.urls import path
from django.contrib.auth import views as auth_views
from .views.allauth_views import CustomPasswordSetView
from .views.views import *
from .views.custom_login_V import *
from .views.custom_login_API_view import CustomLoginAPIView
from .admin_views.custom_user_assign_view_V import *
from .admin_views.users_detail_views import *
from .admin_views.users_list_views import *
from .admin_views.create_users_groups_V import *
from .admin_views.add_other_admins_V import *


urlpatterns = [
    path('your/profile/', profile, name='profile'),
    path('profile/Edit/', profile_edit, name='profile_edit'),
    path('user/login/', LoginView.as_view(), name='custom_login'),
    path('delete-account/', login_required(DeleteAccountView.as_view()), name='delete_account'),
    # =========== Login APIView ===============
    path('api/login/', CustomLoginAPIView.as_view(), name='custom-login-api'),

    # DJANGO-ALLAUTH PASSWORDS_SET VIEW
    path('password/set/', CustomPasswordSetView.as_view(), name='account_set_password'),
    
    # ========ADMIN URLS VIEWS=======================
    path('assign_group/<int:user_id>/', assign_user_group, name='assign_user_group'),
    
    path('Dashboard/users/list/', user_list, name='user_list'),
    path('Dashboard/user/profile/<int:user_id>/', user_detail, name='user_detail'),
    path('Dashboard/user/profile-edit/<int:user_id>/', user_edit, name='user_edit'),
    path('Dashboard/user/profile-edit/<int:user_id>/', custom_admin_view, name='custom_admin_view'),
    
    path('Dashboard/groups/', group_list_view, name='group_list'),
    path('Dashboard/group/<int:pk>/', group_detail, name='group_detail'),
    path('Dashboard/group edit/<int:pk>/', add_group, name='add_group'),
    path('Dashboard/add group/', add_group, name='add_group'),

    path('Dashboard/register/Admin/', register_admins, name='register_admins'),
    
]