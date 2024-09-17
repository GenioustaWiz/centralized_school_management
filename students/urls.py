

from django.urls import path
# ============== admin_views ============
from .admin_views.student_A_views import *
from .admin_views.attendance_A_views import *
from .admin_views.performance_A_views import *
# ============ Views ===========
from .views.student_view import *
from .views.performance_view import *
from .views.attendance_view import *
from .views.student_dashboard import *

urlpatterns = [
    # ============== Students =================
    path('students/list', student_list, name='student_list'),
    path('student/dashboard/<int:pk>/', student_dashboard, name='student_dashboard'),
    # path('student/detail/', student_detail, name='student_detail'),
        # ============== admin_views ============ 
    path('student/add/', edit_add_student, name='edit_add_student'),
    path('student/edit/<int:pk>/', edit_add_student, name='edit_add_student'),
    path('student/delete/<int:pk>/', student_delete, name='student_delete'),
    # ============== Attendance ========================
    path('attendance/', student_list, name='attendance_list'),
    # path(attendance/detail/', student_detail, name='attendance_detail'),
        # ============== admin_views ============
    path('attendance/add/<int:student_id>/', edit_add_attendance, name='edit_add_attendance'),
    # path('attendance/edit/<int:pk>/', edit_add_attendance, name='edit_add_attendance'),
    path('attendance/delete/<int:pk>/', attendance_delete, name='attendance_delete'),
    # ============== Performance ========================
    path('performance/', performance_list, name='performance_list'),
    # path('performance/detail/', performance_detail, name='performance_detail'),
        # ============== admin_views ============
    path('performance/add/<int:student_id>/', edit_add_performance, name='edit_add_performance'),
    path('performance/edit/<int:student_id>/<int:pk>/', edit_add_performance, name='edit_add_performance'),
    path('performance/delete/<int:pk>/', performance_delete, name='performance_delete'),
    
    # ========= For APIViews ============
    path('api/student-list/', StudentListAPIView.as_view(), name='student-list-api'),
    path('api/student-dashboard/<int:pk>/', StudentDashboardAPIView.as_view(), name='student-dashboard-api'),
    # path('api/student/', StudentAPIView.as_view(), name='student_api_views'),
    # path('api/student/', AttendanceAPIView.as_view(), name='student_api_views'),
    # path('api/student/', PerformanceAPIView.as_view(), name='student_api_views'),

]
