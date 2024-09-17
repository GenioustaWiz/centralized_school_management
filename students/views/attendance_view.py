
from django.shortcuts import render, redirect, get_object_or_404
from students.models import Attendance
from accounts.models import User

def attendance_list(request):
    # check if the user is Authenticated
    if request.user.is_authenticated:
        # check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/student/attendance/attendance_list.html'
        else:
            template_name = 'student/attendance/attendance_list.html'
        attendances = Attendance.objects.all()
        context = {
            'attendances': attendances
        }
        return render(request, template_name, context)

def attendance_detail(request):
    # check if the user is Authenticated
    if request.user.is_authenticated:
        # check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/student/attendance/attendance_detail.html'
        else:
            template_name = 'student/attendance/attendance_detail.html'
        attendance = Attendance.objects.all()
        context = {
            'attendance_detail': attendance,
        }
        return render(request, template_name, context)
