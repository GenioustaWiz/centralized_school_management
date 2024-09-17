from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from students.models import Student, Attendance, Performance
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from students.serializers.student_dashboard_s import StudentSerializer, AttendanceSerializer, PerformanceSerializer

@login_required
def student_dashboard(request, pk=None):
    #check if the user is authenticated
    if request.user.is_authenticated:
        # check the user's type, for access limitations
        if request.user.is_superuser or request.user.user_type in ['master_admin', 'lead_admin', 'data_admin']:
            template_name = 'maindashboard/student/student_dashboard.html'
        else:
            template_name = 'student/student_dashboard.html'

        student = get_object_or_404(Student, pk=pk)
            
        # Fetch attendance data
        attendance_data = Attendance.objects.filter(student=student).values('status').annotate(value=Count('status'))
        
        # Fetch performance data
        performance_data = Performance.objects.filter(student=student).values('subject', 'grade')
        
        # Fetch recent attendance
        recent_attendance = Attendance.objects.filter(
            student=student,
            date__gte=timezone.now().date() - timedelta(days=30)
        ).order_by('-date')[:5]

        # Fetch recent performance
        recent_performance = Performance.objects.filter(
            student=student,
            assessment_date__gte=timezone.now().date() - timedelta(days=30)
        ).order_by('-assessment_date')[:5]
        
        context = {
            'student': student,
            'attendance_data': list(attendance_data),
            'performance_data': list(performance_data),
            'recent_attendance': recent_attendance,
            'recent_performance': recent_performance,
        }
        
        return render(request, template_name, context)

# ======================== APIView ==============================
class StudentDashboardAPIView(APIView):
    def get(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)

        # Fetch attendance data
        attendance_data = Attendance.objects.filter(student=student).values('status').annotate(value=Count('status'))

        # Fetch performance data
        performance_data = Performance.objects.filter(student=student).values('subject', 'grade')

        # Fetch recent attendance
        recent_attendance = Attendance.objects.filter(
            student=student,
            date__gte=timezone.now().date() - timedelta(days=30)
        ).order_by('-date')[:5]

        # Fetch recent performance
        recent_performance = Performance.objects.filter(
            student=student,
            assessment_date__gte=timezone.now().date() - timedelta(days=30)
        ).order_by('-assessment_date')[:5]

        context = {
            'student': StudentSerializer(student).data,
            'attendance_data': list(attendance_data),
            'performance_data': list(performance_data),
            'recent_attendance': AttendanceSerializer(recent_attendance, many=True).data,
            'recent_performance': PerformanceSerializer(recent_performance, many=True).data,
        }

        return Response(context)
        # serializer = StudentSerializer(student, context={'attendance_data': attendance_data, 'performance_data': performance_data})
        # return Response(serializer.data)