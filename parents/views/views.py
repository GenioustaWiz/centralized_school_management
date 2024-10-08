from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required 
import json
from django.core.serializers.json import DjangoJSONEncoder

from parents.models import Parent
from students.models import Student, Attendance, Performance

@login_required
def parent_detail(request):
    user = request.user
    
    if user.user_type == 'parent':
        template_name = 'parent/parent_dashboard.html'
    else:
        return HttpResponseForbidden("You don't have permission to access this page.")

    try:
        parent = Parent.objects.get(user=user)
    except Parent.DoesNotExist:
        return render(request, template_name, {'error_message': "No parent profile found for this user."})

    students = Student.objects.filter(parent=parent)

    if not students.exists():
        return render(request, template_name, {'parent': parent, 'warning_message': "No students are registered under you."})

    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)

    student_data = []
    for student in students:
        daily_attendance = Attendance.objects.filter(student=student, date=today).first()
        weekly_attendance = list(Attendance.objects.filter(student=student, date__gte=week_ago).values('status').annotate(value=Count('status')))
        overall_performance = Performance.objects.filter(student=student).aggregate(Avg('grade'))['grade__avg']
        monthly_performance = list(Performance.objects.filter(student=student, assessment_date__gte=month_ago).values('assessment_date', 'subject', 'grade'))

        student_data.append({
            'student_id' : student.id,
            'student': student.first_name + " " + student.last_name,
            'daily_attendance': daily_attendance.status if daily_attendance else 'N/A',
            'weekly_attendance': weekly_attendance,
            'overall_performance': overall_performance or 'N/A',
            'monthly_performance': monthly_performance
        })

        print(f"student_data: {student_data}")
        print("++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++")
    
    context = {
        'parent': parent,
        'student_data_json': json.dumps(student_data, cls=DjangoJSONEncoder),
    }
    return render(request, template_name, context)

